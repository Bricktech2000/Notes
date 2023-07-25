# Notes

_A repository of my conceptual notes_

[View Published Notes](https://notes.emilien.ca/)

## Taking Notes

Notes are a way to have quick access to lots of relevant information. We don't care about the notes themselves; we care about the information.

During lectures, don't take notes for U-S-E information:

- Unimportant
- Self-Explanatory
- Easy to Memorize

If you think you don't really have to write something down, you probably don't have to write it down.

Since examples aren't an ideal way to store information, only write down general examples that help you understand. During lectures, try to predict what the teacher will do, and only take notes when the teacher does something you found unexpected.

This promotes active learning, meaning you are studying while attending class. Moreover, questions will come up in real time rather than when it's too late to ask.

## Conceptual Notes

Even though the teacher is giving you a story in a lecture, look for concepts instead. Make notes as atomic as possible, so that you can link to a concept from other concepts. If you think about it, this is exactly how your brain stores information: a sea of concepts linked together. Moreover, instead of arbitrarily splitting concepts into disciplines, this approach allows the creation of numerous links between all aspects of your life, encouraging innovation.

Writing atomically also allows for easy reorganization of your notes during the lecture itself. Paper notes are almost always taken sequentially, as it is not possible to reorganize information efficiently as it is flying by during lectures.

Taking notes conceptually allows you to build on top of your older notes and make them grow and evolve instead of letting them slowly decay over time.

## Conventions

For conventions on writing notes, see the [conventions](https://notes.emilien.ca/conventions) page.

## Publishing

The publishing workflow for my conceptual notes requires [mkdocs](https://www.mkdocs.org/).

Once installed, run the following commands:

```bash
rm -r site; rm mkdocs/*.md; rm mkdocs/*.png; rm mkdocs/*.jpg; rm mkdocs/*.gif; rm mkdocs/*.pdf;
python3 mkdocs.py notes mkdocs && mkdocs build
python3 -m http.server --directory site
```
