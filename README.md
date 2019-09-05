# teaching-coding
this is a repo to guide young padawans in the right direction, no more no less

## Introduction
This is not teaching any one language to a full extend, this is about teaching good best-practices right from the beginning. And to learn about tools to make a devs life easier, because ultimately we are all lazy at heart ;)

## Some Conventions
* Comments in source should when possible be always done to enable multiline editing right of the bat, so that when docstrings get expanded their enclosing syntax doesnt have to be changed retroactively. Remember: Smart design choices from the start are better than refactoring. Always! And this starts with "small" things like comments/docstrings
* If a language requires/recommends a specific directory/file layout, it is wise to stick tothese, to prevent stupid errors from cropping up, just to satisfy ones own need to name it after something dear to the heart ;) This goes actually back again to the above, when possible avoid refactoring, this is even more painful when you have to rename a whole slew of files/directories retrospectively
* Last but not least, this is meant to fun more than anything, if i wanted to create s simple "how-to learn programming language x" i could just point my ward towards any number of 100s of tutorials. Here you are learning good habbits and independance(?)
** Addendum: If you want to suggest any changes, don't hesitate to clone, branch and commit/push back into this repo, this is a collaborative work

# The app
According to python documentation one wants to create a certain directory structrure.
I have in this specific case done exactly that - rtfm - take what you see as a "sane" default to start your project, or a template if you will.
One should be able to again clone and then ```python3 app/calculator.py```

# The test(s)
This is where it ultimately comes to ones own taste in toolkits, every dev, over time, will develop their own (almost) "ready-to-go" toolkit that they will draw upon again and again.
* caveat emptor! don't fall into the trap of never re-evaluating your own toolkit! seriously! being a _good_ dev means to be able to be critical about oneself before anything else. A humble developer, willing to drink new knowledge will at the end of the day, always learn more, be more, and yes of course also most likely earn more :P

If one quickly checks out the Pipfile you'll see a reference to a package called "nose" (also refered to as nosetest)
This is our test-framework in this case, again for almost every language you will find there is a multitude of different frameworks for everything.
** Javascript (and unfortunately by extension also NodeJS) are really suffering really from this, where for almost every common dev problem there exists (without a joke) 100s of packages/framework and their interdependencies are beyond a joke. Yes package-managers can mitigate some of this cruft but imho when the total number of (so-called "established") frameworks is in the high thousands it is almost like trying to re-invent the wheel again and again and expecting different results ;)

* Oh yes: the tests are not working currently, my last few commits were mostly, cleanup, refactoring and documentation ;)