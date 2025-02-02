/*
 * mptest.c: test rig and example code for the metaprogramming
 * mechanism in mp.h.
 *
 * Accompanies the article on the web at
 *   https://www.chiark.greenend.org.uk/~sgtatham/mp/
 */

/*
 * mptest.c is copyright 2012 Simon Tatham.
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT.  IN NO EVENT SHALL SIMON TATHAM BE LIABLE FOR
 * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * 
 * $Id$
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "mp.h"

#ifdef C89
#define HOPEFULLY_DECLARE_AS_INT(x)
int _i;
#else
#define HOPEFULLY_DECLARE_AS_INT(x) int x
#endif

/*
 * General test loops to exercise a lot of the macros.
 */
#define TEST_LOOP_1(loopvar, start, limit)                      \
    MPP_DECLARE(1, HOPEFULLY_DECLARE_AS_INT(_i))                \
    MPP_BEFORE(2, printf("preloop\n"); _i = start)              \
    MPP_AFTER(3, printf("postloop\n"))                          \
    MPP_WHILE(4, _i < limit)                                    \
    MPP_BREAK_CATCH(5)                                          \
    MPP_BEFORE(6, printf("preiter %d\n", _i))                   \
    MPP_AFTER(7, printf("postiter %d\n", _i); _i++)             \
    MPP_DECLARE(8, loopvar = _i + 100)                          \
    MPP_BREAK_THROW(5)                                          \
    MPP_BREAK_HANDLER(9, printf("break!\n"))                    \
    MPP_FINALLY(10, printf("finally\n"))

#define TEST_LOOP_2(loopvar, start, limit)                      \
    MPP_DECLARE(1, HOPEFULLY_DECLARE_AS_INT(_i))                \
    MPP_BEFORE(2, printf("preloop\n"); _i = start)              \
    MPP_AFTER(3, printf("postloop\n"))                          \
    MPP_DO_WHILE(4, _i < limit)                                 \
    MPP_BREAK_CATCH(5)                                          \
    MPP_BEFORE(6, printf("preiter %d\n", _i))                   \
    MPP_AFTER(7, printf("postiter %d\n", _i); _i++)             \
    MPP_DECLARE(8, loopvar = _i + 100)                          \
    MPP_BREAK_THROW(5)                                          \
    MPP_BREAK_HANDLER(9, printf("break!\n"))                    \
    MPP_FINALLY(10, printf("finally\n"))

/*
 * for_general out of the document.
 */
#define for_general(init, firstcond, nextcond, increment)       \
    MPP_DECLARE(1, init)                                        \
    MPP_IF(2, firstcond)                                        \
    MPP_DO_WHILE(3, nextcond)                                   \
    MPP_BREAK_CATCH(4)                                          \
    MPP_AFTER(5, increment)                                     \
    MPP_BREAK_THROW(4)

/*
 * WHILE_ELSE: a modified while that accepts an else clause. Does
 * _not_ have the Python semantics (else clause run at the very end of
 * the loop unless skipped by break): instead, the else clause is run
 * if and only if the condition _starts off_ false, i.e. if the loop
 * body is run zero times.
 *
 * The idea is that this would be used in cases such as printing a
 * human-readable diagnostic per action taken, when it might be seen
 * as unfriendly not to print a message if no actions were taken at
 * all. So, for instance,
 *
 *     WHILE_ELSE (there's a thing to do) {
 *         printf("Processing thing %s\n", name_of_thing());
 *         process_thing();
 *     } else {
 *         printf("There were no things to process\n");
 *     }
 */
#define WHILE_ELSE(condition)                   \
    MPP_ELSE_ACCEPT(1)                          \
    if (!(condition)) MPS_ELSE_INVOKE(1); else  \
        MPP_DO_WHILE(2, condition)

/*
 * FOR_ELSE: a modified for that accepts an else clause. Has the
 * Python semantics: else clause is run at the end of the loop except
 * that 'break' skips it.
 *
 * Used in cases where you're searching for a thing in a list, and
 * break when you find it. Then the else clause is run if and only if
 * the thing wasn't found.
 *
 * (Of course, this would be more robust using a C99 variadic macro
 * for the argument list, so that the macro didn't choke on
 * unprotected commas. For the sake of making this test program still
 * work in C89, I haven't done that in this example.)
 *
 *     FOR_ELSE (i = 0; i < n; i++) {
 *         if (array[i] is the droid we're looking for)
 *             break;
 *     } else {
 *         move_along();
 *     }
 *
 */
#define FOR_ELSE(for_arguments)                 \
    MPP_ELSE_ACCEPT(1)                          \
    MPP_BREAK_STOP(2, (void)0)                  \
    MPP_BREAK_CATCH(3)                          \
    MPP_AFTER(4, MPS_ELSE_INVOKE(1))            \
    for (for_arguments)                         \
        MPP_BREAK_THROW(3)

/*
 * WHILE_INTERLEAVED ... WITH: a control structure for all those times
 * you want to do the main thing n times and an intervening thing n-1
 * times. Usually this comes up when printing stuff with separators in
 * between, for which I usually use a variable:
 *
 *   sep = "";
 *   while (condition) {
 *       printf("%s%s", sep, thing);
 *       sep = ",";
 *   }
 *
 * which gets me commas in between the things, and always one fewer
 * commas than things (unless there were zero things).
 *
 * Wouldn't it be nicer to be able to get rid of that ugly state
 * variable, and write this?
 *
 *   WHILE_INTERLEAVED (condition) {
 *       printf("%s", thing);
 *   } WITH {
 *       putchar(',');
 *   }
 *
 * This is a pretty fiddly one to implement, since you have to arrange
 * correct handling of the four possibilities 'else clause
 * terminates', 'else clause breaks', 'main clause terminates' and
 * 'main clause breaks'. I use MPP_ELSE_GENERAL for the former two,
 * followed by MPP_AFTER and MPP_BREAK_THROW to handle the latter two.
 */
#define WHILE_INTERLEAVED(condition)                                    \
    MPP_IF(1, condition)                                                \
    MPP_WHILE(2, 1)                                                     \
    MPP_BREAK_CATCH(3)                                                  \
    MPP_ELSE_GENERAL(4, MPS_MAIN_INVOKE(4), MPS_BREAK_THROW(3))         \
    MPP_AFTER(5, if (condition) MPS_ELSE_INVOKE(4); else MPS_BREAK_THROW(3)) \
    MPP_BREAK_THROW(3)

#define WITH else          /* a cheap piece of syntactic saccharine */

#ifndef C89

/*
 * Extended example showing the FOR_EACH_HIPPO macro from the
 * accompanying article.
 */

static const char *const hippo_names[] = {
    "Jack", "Irene", "Henry", "Gemma", "Fred",
    "Elaine", "Derek", "Catherine", "Ben", "Anna",
};

typedef struct {
    int index, remaining, allocated, freed;
} hippo_retrieval_context;

typedef struct {
    int index;
    const char *name;
} hippo;

static int next_index = 100;

hippo_retrieval_context *new_hippo_retrieval_context(void)
{
    hippo_retrieval_context *hc =
        (hippo_retrieval_context *)malloc(sizeof(hippo_retrieval_context));
    hc->remaining = 10;
    hc->allocated = hc->freed = 0;
    hc->index = next_index++;
    printf("new context %d\n", hc->index);
    return hc;
}

void free_hippo_retrieval_context(hippo_retrieval_context *hc)
{
    printf("freeing context %d (remaining=%d, allocated=%d, freed=%d)\n",
           hc->index, hc->remaining, hc->allocated, hc->freed);
    assert(hc->allocated == hc->freed);
    free(hc);
}

int hippo_available(hippo_retrieval_context *hc)
{
    printf("checking availability in %d (%d => %s)\n",
           hc->index, hc->remaining, hc->remaining > 0 ? "yes" : "no");
    return hc->remaining > 0;
}

hippo *get_hippo(hippo_retrieval_context *hc)
{
    hippo *h;
    
    assert(hc->remaining > 0);
    h = (hippo *)malloc(sizeof(hippo));
    h->index = next_index++;
    h->name = hippo_names[--hc->remaining];
    printf("allocated hippo %d (name=%s) from %d\n", h->index,
           h->name, hc->index);
    hc->allocated++;
    return h;
}

void free_hippo(hippo_retrieval_context *hc, hippo *h)
{
    printf("freeing hippo %d from %d\n", h->index, hc->index);
    free(h);
    hc->freed++;
}

#define FOR_EACH_HIPPO(loopvar)                                 \
    MPP_DECLARE(1, hippo_retrieval_context *_hc)                \
    MPP_BEFORE(2, _hc = new_hippo_retrieval_context())          \
    MPP_AFTER(3, free_hippo_retrieval_context(_hc))             \
    MPP_WHILE(4, hippo_available(_hc))                          \
    MPP_BREAK_CATCH(5)                                          \
    MPP_DECLARE(6, hippo *_h = get_hippo(_hc))                  \
    MPP_DECLARE(7, loopvar = _h)                                \
    MPP_BREAK_THROW(5)                                          \
    MPP_FINALLY(8, free_hippo(_hc, _h))

/*
 * Coroutine-based example. I define a set of coroutine macros here
 * which are slightly different from the 'Coroutines in C' example
 * code, because it's convenient to have the state structure be
 * defined in the calling scope.
 */
#define MPCR_BEGIN switch (s->_line) { case 0:
#define MPCR_END(dummyval) s->_line = -1; }
#define MPCR_YIELD(value) do                    \
    {                                           \
        s->_line = __LINE__;                    \
        s->_val = (value);                      \
        return;                                 \
      case __LINE__:;                           \
    } while (0)

/*
 * State structure and iterator function for the loop.
 */
struct twothree_state {
    int _line, _val;
    int limit;
    int i;
};
void twothree_iterator(struct twothree_state *s)
{
    int tmp;
    MPCR_BEGIN;
    for (s->i = 1; s->i < s->limit; s->i *= 2) {
        MPCR_YIELD(s->i);
        if (s->i > 1) {
            tmp = s->i + (s->i >> 1);
            if (tmp < s->limit)
                MPCR_YIELD(tmp);
        }
    }
    MPCR_END(0);
}

/*
 * Loop macro which calls it.
 */
#define TWOTHREE_UP_TO(loopvar, limitval)               \
    MPP_DECLARE(1, struct twothree_state _state)        \
    MPP_BEFORE(2, _state._line = 0;                     \
               _state.limit = limitval;                 \
               twothree_iterator(&_state))              \
    MPP_WHILE(3, _state._line >= 0)                     \
    MPP_BREAK_CATCH(4)                                  \
    MPP_AFTER(5, twothree_iterator(&_state))            \
    MPP_DECLARE(6, loopvar = _state._val)               \
    MPP_BREAK_THROW(4)

/*
 * Equivalent ordinary function that does the printing itself.
 */
void twothree_up_to(int limit)
{
    int i, tmp;
    for (i = 1; i < limit; i *= 2) {
        printf("twothree: %d\n", i); /* a power of 2 */
        if (i > 1) {
            tmp = i + (i >> 1);
            if (tmp < limit)
                printf("twothree: %d\n", tmp); /* 3 times a power of 2 */
        }
    }
}

#endif /* C89 */

int main(void)
{
    int j, z;

    /*
     * Basic test. We expect j to range from 100 to 109 inclusive, to
     * see a preloop/postloop pair surrounding each loop, and to see a
     * preiter/postiter pair surrounding each iteration and citing a
     * value 100 less than j.
     */
#ifndef EXPECTED
    TEST_LOOP_1(j, 0, 10) printf("got %d\n", j);
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

    /*
     * Same test but with braces around the statement. Should work
     * identically.
     */
#ifndef EXPECTED
    TEST_LOOP_1(j, 0, 10) { printf("got %d\n", j); }
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

    /*
     * Basic test of the do-while version.
     */

#ifndef EXPECTED
    TEST_LOOP_2(j, 0, 10) printf("got %d\n", j);
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

    /*
     * Test the difference between MPP_WHILE and MPP_DO_WHILE.
     */
#ifndef EXPECTED
    TEST_LOOP_1(j, 0, 0) printf("got %d\n", j);
    TEST_LOOP_2(j, 0, 0) printf("got %d\n", j);
    TEST_LOOP_1(j, 0, 1) printf("got %d\n", j);
    TEST_LOOP_2(j, 0, 1) printf("got %d\n", j);
#else
    printf("preloop\npostloop\n");     /* loop 1 with start==limit is empty */
    /* all three other loops should do one iteration */
    printf("preloop\npreiter 0\ngot 100\nfinally\npostiter 0\npostloop\n");
    printf("preloop\npreiter 0\ngot 100\nfinally\npostiter 0\npostloop\n");
    printf("preloop\npreiter 0\ngot 100\nfinally\npostiter 0\npostloop\n");
#endif

    /*
     * Test 'break' in each loop type. We expect postiter to be
     * bypassed, but the break handler should run and then postloop
     * should run.
     */
#ifndef EXPECTED
    TEST_LOOP_1(j, 0, 10) {
        printf("got %d\n", j);
        if (j == 102)
            break;
    }
#else
    printf("preloop\n");
    printf("preiter 0\ngot 100\nfinally\npostiter 0\n");
    printf("preiter 1\ngot 101\nfinally\npostiter 1\n");
    printf("preiter 2\ngot 102\nfinally\nbreak!\n");
    printf("postloop\n");
#endif

#ifndef EXPECTED
    TEST_LOOP_2(j, 0, 10) {
        printf("got %d\n", j);
        if (j == 102)
            break;
    }
#else
    printf("preloop\n");
    printf("preiter 0\ngot 100\nfinally\npostiter 0\n");
    printf("preiter 1\ngot 101\nfinally\npostiter 1\n");
    printf("preiter 2\ngot 102\nfinally\nbreak!\n");
    printf("postloop\n");
#endif

    /*
     * Test 'continue' in each loop type. We expect the postiter to
     * still run and the loop to continue.
     */
#ifndef EXPECTED
    TEST_LOOP_1(j, 0, 10) {
        printf("got %d\n", j);
        if (j == 102)
            continue;
        printf("still got %d\n", j);
    }
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++) {
        if (j == 2)
            printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
        else
            printf("preiter %d\ngot %d\nstill got %d\nfinally\npostiter %d\n",
                   j, j+100, j+100, j);
    }
    printf("postloop\n");
#endif

#ifndef EXPECTED
    TEST_LOOP_2(j, 0, 10) {
        printf("got %d\n", j);
        if (j == 102)
            continue;
        printf("still got %d\n", j);
    }
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++) {
        if (j == 2)
            printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
        else
            printf("preiter %d\ngot %d\nstill got %d\nfinally\npostiter %d\n",
                   j, j+100, j+100, j);
    }
    printf("postloop\n");
#endif

    /*
     * Test for_general.
     */
    printf("for_general tests\n");
#ifndef EXPECTED
    /* This loop shouldn't run at all because the initial test fails */
    for_general (j = 0, j != 0, j < 10, j++) printf("first %d\n", j);
    /* This loop should run to completion, proving that the initial test
     * is not re-run after subsequent loop iterations */
    for_general (j = 0, j != 5, j < 10, j++) printf("second %d\n", j);
    /* This loop should run ten times, proving that the iteration test
     * is not run at the start */
    for_general (j = 0, 1, j % 10 != 0, j++) printf("third %d\n", j);
    /* This loop should terminate at the break, proving that I haven't
     * broken break. */
    for_general (j = 0, 1, j % 10 != 0, j++) {
        printf("fourth %d\n", j);
        if (j == 7)
            break;
    }
    /* This loop should skip one print but still run sensibly, proving
     * that 'continue' doesn't skip the increment.. */
    for_general (j = 0, 1, j % 10 != 0, j++) {
        if (j == 4)
            continue;
        printf("fifth %d\n", j);
    }
#else
    for (j = 0; j < 10; j++) printf("second %d\n", j);
    for (j = 0; j < 10; j++) printf("third %d\n", j);
    for (j = 0; j <= 7; j++) printf("fourth %d\n", j);
    for (j = 0; j < 10; j++) if (j != 4) printf("fifth %d\n", j);
#endif

#ifndef C89
    /*
     * Test declarations (only in C99 mode).
     */
#ifndef EXPECTED
    TEST_LOOP_1(int k, 0, 10) printf("got %d\n", k);
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

#ifndef EXPECTED
    TEST_LOOP_2(int k, 0, 10) printf("got %d\n", k);
#else
    printf("preloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif
#endif

    /*
     * Verify that the syntactic form of the whole expression is of a
     * single statement, by ensuring we can enclose one in an if-else.
     */
#ifndef EXPECTED
    for (z = 0; z < 2; z++)
        if (z)
            TEST_LOOP_1(j, 0, 10) printf("got %d\n", j);
        else
            printf("skipping\n");
#else
    printf("skipping\npreloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

#ifndef EXPECTED
    for (z = 0; z < 2; z++)
        if (z)
            TEST_LOOP_2(j, 0, 10) printf("got %d\n", j);
        else
            printf("skipping\n");
#else
    printf("skipping\npreloop\n");
    for (j = 0; j < 10; j++)
        printf("preiter %d\ngot %d\nfinally\npostiter %d\n", j, j+100, j);
    printf("postloop\n");
#endif

    /*
     * Test WHILE_ELSE, both with and without an else clause.
     *
     * gcc will generate an annoying warning if you use it without an
     * else, on the grounds that the construction fundamentally relies
     * on the (correct) resolution of the if-else ambiguity and gcc
     * warns if you write code that depends on that at all. Of course
     * you can just write 'while' instead of WHILE_ELSE if you didn't
     * want an else clause anyway, but still, bah.
     */
#ifndef EXPECTED
    j = 0;
    WHILE_ELSE(j < 2)
        printf("got %d\n", j++);
    else
        printf("got nothing\n");
    WHILE_ELSE(j < 2)
        printf("got %d\n", j++);
    else
        printf("got nothing\n");
    j = 0;
    WHILE_ELSE(j < 2)
        printf("got %d\n", j++);
    WHILE_ELSE(j < 2)
        printf("got %d\n", j++);
#else
    printf("got 0\ngot 1\n");          /* 2 iterations, else clause */
    printf("got nothing\n");           /* 0 iterations, else clause */
    printf("got 0\ngot 1\n");          /* 2 iterations, no else clause */
    /* 0 iterations, no else clause, nothing printed */
#endif

    /*
     * Test FOR_ELSE, again with and without an else clause.
     *
     * As above, calls without an else clause generate a gcc warning.
     */
#ifndef EXPECTED
    FOR_ELSE (j = 0; j < 10; j++) {
        printf("trying %d\n", j); 
        if (j == 3) {
            printf("found it\n");
            break;
        }
    } else {
        printf("not found\n");
    }

    FOR_ELSE (j = 0; j < 10; j++) {
        printf("trying %d\n", j); 
        if (j == 13) {
            printf("found it\n");
            break;
        }
    } else {
        printf("not found\n");
    }

    FOR_ELSE (j = 0; j < 10; j++) {
        printf("trying %d\n", j); 
        if (j == 3) {
            printf("found it\n");
            break;
        }
    }

    FOR_ELSE (j = 0; j < 10; j++) {
        printf("trying %d\n", j); 
        if (j == 13) {
            printf("found it\n");
            break;
        }
    }
#else
    for (j = 0; j <= 3; j++)
        printf("trying %d\n", j);
    printf("found it\n");
    for (j = 0; j < 10; j++)
        printf("trying %d\n", j);
    printf("not found\n");
    for (j = 0; j <= 3; j++)
        printf("trying %d\n", j);
    printf("found it\n");
    for (j = 0; j < 10; j++)
        printf("trying %d\n", j);
#endif

    /*
     * Test WHILE_INTERLEAVED.
     */
#ifndef EXPECTED
    for (z = 0; z < 5; z++) {
        printf("Loop with limit %d: ", z);
        j = 0;
        WHILE_INTERLEAVED(j < z)
            printf("%d", j++);
        WITH
            putchar(',');
        putchar('\n');
        printf("Loop with limit %d breaking at 2: ", z);
        j = 0;
        WHILE_INTERLEAVED(j < z) {
            printf("%d", j);
            if (j == 2)
                break;
            j++;
        } WITH
              putchar(',');
        putchar('\n');
        printf("Loop with limit %d breaking at 3 in with clause: ", z);
        j = 0;
        WHILE_INTERLEAVED(j < z)
            printf("%d", j++);
        WITH {
            if (j == 3)
                break;
            putchar(',');
        }
        putchar('\n');
    }
#else
    printf("Loop with limit 0: \n");
    printf("Loop with limit 0 breaking at 2: \n");
    printf("Loop with limit 0 breaking at 3 in with clause: \n");
    printf("Loop with limit 1: 0\n");
    printf("Loop with limit 1 breaking at 2: 0\n");
    printf("Loop with limit 1 breaking at 3 in with clause: 0\n");
    printf("Loop with limit 2: 0,1\n");
    printf("Loop with limit 2 breaking at 2: 0,1\n");
    printf("Loop with limit 2 breaking at 3 in with clause: 0,1\n");
    printf("Loop with limit 3: 0,1,2\n");
    printf("Loop with limit 3 breaking at 2: 0,1,2\n");
    printf("Loop with limit 3 breaking at 3 in with clause: 0,1,2\n");
    printf("Loop with limit 4: 0,1,2,3\n");
    printf("Loop with limit 4 breaking at 2: 0,1,2\n");
    printf("Loop with limit 4 breaking at 3 in with clause: 0,1,2\n");
#endif

#ifndef C89
    /*
     * Test FOR_EACH_HIPPO against the sample code that you might
     * write in the absence of loop metaprogramming.
     */
#ifndef EXPECTED
    FOR_EACH_HIPPO (hippo *h)
        printf("We have a hippo called %s\n", h->name);

    FOR_EACH_HIPPO (hippo *h) {
        printf("Checking %s\n", h->name);
        if (h->name[0] == 'G') {
            printf("%s matched\n", h->name);
            break;
        }
        printf("%s didn't match\n", h->name);
    }
#else
    {
        hippo_retrieval_context *hc;
        hc = new_hippo_retrieval_context();
        while (hippo_available(hc)) {
            hippo *h = get_hippo(hc);
            printf("We have a hippo called %s\n", h->name);
            free_hippo(hc, h);
        }
        free_hippo_retrieval_context(hc);
    }

    {
        hippo_retrieval_context *hc;
        hc = new_hippo_retrieval_context();
        while (hippo_available(hc)) {
            hippo *h = get_hippo(hc);
            printf("Checking %s\n", h->name);
            if (h->name[0] == 'G') {
                printf("%s matched\n", h->name);
                free_hippo(hc, h);
                break;
            }
            printf("%s didn't match\n", h->name);
            free_hippo(hc, h);
        }
        free_hippo_retrieval_context(hc);
    }
#endif

    /*
     * Test the coroutines example. This generates powers of 2 and
     * one-and-a-half times powers of 2, up to a given limit. We
     * demonstrate 'break' working too, of course.
     */
#ifndef EXPECTED
    TWOTHREE_UP_TO(int k, 1000)
        printf("twothree: %d\n", k);
    TWOTHREE_UP_TO(int k, 1200)
        printf("twothree: %d\n", k);
    TWOTHREE_UP_TO(int k, 1000) {
        if (k >= 300)
            break;
        printf("twothree: %d\n", k);
    }
#else
    twothree_up_to(1000);
    twothree_up_to(1200);
    twothree_up_to(300);
#endif

#endif /* C89 */

    return 0;
}
