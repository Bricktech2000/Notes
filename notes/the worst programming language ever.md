# The Worst Programming Language Ever

---

# History

---

## COBL

```COBL
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
  DISPLAY 'Hello, world'.
  STOP RUN.
```

---

## IBM COBL

```COBOL
//COBUCLG JOB CLASS=A, MSGCLASS=A, MSGLEVEL=(1,1)
//HELOWRLD EXEC COBUCLG, PARM.COB='MAP, LIST, LET'
//COB. SYSIN DD *
  001  IDENTIFICATION DIVISION.
  002  PROGRAM-ID.   'HELLO'.
  003  ENVIRONMENT DIVISION.
  004  CONFIGURATION SECTION
  005  SOURCE-COMPUTER.   IBM-360.
  006  OBJECT-COMPUTER.   IBM-360.
  0065 SPECIAL-NAMES.
  0066     CONSOLE IS CNSL.
  007  DATA DIVISION.
  008  WORKING-STORAGE SECTION.
  009  77  HELLO-CONST   PIC X(12) VALUE 'HELLO, WORLD'.
  075  PROCEDURE DIVISION.
  090  000-DISPLAY.
  100      DISPLAY HELLO-CONST UPON CNSL.
  110      STOP RUN.
//LKED. SYSLIB DD DSNAME=SYS1. COBLIB, DISP=SHR
//             DD DSNAME=SYS1.LINKLIB, DISP=SHR
//GO.SYSPRINT DD SYSOUT=A
//
```

---

## APL

_a programming language_

```APL
'Hello, World!'
```

---

## APL

_a programming language_

```APL
life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵}
```

---

## APL

_a programming language_

![[20220728222610.jpg]]

---

## INTERCAL

```INTERCAL
DO ,1 <- #13
PLEASE DO ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #112
DO ,1 SUB #4 <- #0
DO ,1 SUB #5 <- #64
DO ,1 SUB #6 <- #194
DO ,1 SUB #7 <- #48
PLEASE DO ,1 SUB #8 <- #22
DO ,1 SUB #9 <- #248
DO ,1 SUB #10 <- #168
DO ,1 SUB #11 <- #24
DO ,1 SUB #12 <- #16
DO ,1 SUB #13 <- #162
PLEASE READ OUT ,1
PLEASE GIVE UP
```

---

## Visual Basic

![[20220728223429.png]]

---

## Gupta SQLWindows

![[20220728223540.png]]

---

# ...

---

# BS

---

<br />

<br />

# BS

Why?

Because F\*\*\* You, That's Why.

---

## Design Principles

---

## Design Principles

- Create the "Booby-trapped Aztec Temple of Fail"
- Don't trust the programmer to get simple things right
- Leave all the really complicated stuff to the programmer to get right
- Try to do everything
  - Low-level systems
  - Embedded
  - Rich GUIs
  - Web
  - Devices
  - IoT
  - VR
  - Furby
  - ...

---

## Inspiration

---

let's stop here. this is such an unorganized talk
