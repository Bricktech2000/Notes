# ADT Organization

**see** [[abstract data type]], [[algebraic structure]]

there seems to exist some sort of a [[category#isomorphism]] between [[abstract data type]]s and information organization. I use the term _isomorphism_ loosely in this context to refer to the fact that knownedge can be losslessly tranlsated between the two [[concept]]s

> **example** _isomorphisms between [[abstract data type]]s and information organization_
>
> - [[book]]s are [[array]]s. it is hard to look up data stored on an unknown page of a [[book]], and it is hard to find a specific item in an [[array]]. the table of contents of a [[book]] is a [[map]] that can be used to find data in the [[book]]
> - sequential notes are a [[set]] of [[linked list]]s or [[array]]s, depending on whether the notes are digital. most people use one notebook per subject, which creates a [[set]]. sequential notes are taken sequentially, which forms a [[list]]
> - conceptual notes are a [[graph]] of [[tree]]s. every [[concept]] is organized by the [[set]] of [[concept]]s it is related to, which forms a [[graph]]. each [[concept]] is divided into multiple levels of subtitles within one file, which creates a [[tree]]
> - a file system is a [[tree]], or a [[set]] of [[set]]s of [[set]]s of items. this is self-explanatory. if the files within a folder are sorted by some metric, then the file system becomes a [[list]] of [[list]]s of [[list]]s of items

> **example** _translating between [[abstract data type]]s and information organization through isomorphisms_
>
> I tried to organize my files in vairous categories such as _finance_ and _programming_, which really didn't work that well. a project such as my resume is related to _finance_ because it is used to apply to jobs, but is also related to _programming_ because I built it in [[markdown]] and [[python]]. even worse is that sorting my files in those categories made it such a hassle to find them: I always knew their name but never knew in which category I put them. looking back, a [[tree]] [[abstract data type]] was the wrong choice
>
> thinking in terms of [[abstract data type]]s, what I really need is a [[map]] from project name to project data, along with a way to easily access most active projects, such as a [[priority queue]]. most of the time, project data is most easily stored as a [[tree]]. translating this logic to file systems, the result is one large single-level folder sorted by date containing folders containing project data. project data folders are automatically [[tree]]s, the fact that the root folder is sorted by date means that most active projects will be easy to access, and the fact that I mostly use the command line makes the `cd` command a [[map]] from project name to project data
