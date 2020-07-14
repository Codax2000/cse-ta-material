# Classes and Modules
### Alex
These two classes are meant to be practice for writing objects in Python.
The `SuitJacket` class tracks basic data of a men's suit jacket, and the
`Closet` class uses and orders the `SuitJacket` class, something like
the `SearchEngine` uses the `Document` class. This challenge is meant
to be a little light-hearted practice.

## Intro
It is a little-known fact that men's fashion has a tremendous amount of
tradition behind it. Most every article of men's fancy clothing has a
history or a set of rules behind it. This is best shown in the jackets.

People have very strong opinions about men's jacket's and which are the best,
so you will write a program to keep track of just such jackets, to help
keep track of this difficult issue.

## SuitJacket
Write a `SuitJacket` class that somebody could use to classify a men's jacket.
It should keep track of:
1. The number of 'vents' the jacket has, which will be either 0, 1, or 2
 * We're not making this up. If you're curious about vents and men's jackets,
   see [here](https://www.linkedin.com/pulse/should-you-choose-single-double-vent-suit-jacket-dan-thomas/)
2. The number of buttons on the front of the jacket
3. The pattern of the jacket, as a `String`

The `SuitJacket` class's constructor should take a `String`
specifying the type of the jacket, an `int` as the number of
vents, an `int` specifying the number of front buttons. The default number
of front buttons should be 3.

The `SuitJacket` class should have the following methods:
1. `get_type()`
  * This method should return the pattern of the jacket and take no parameters.
2. `get_style_score()`
  * This method should score the jacket based on the number of buttons
    and vents.
  * The score should be calculated by adding the number of buttons
    by the number of vents.

Here is a sample of how a `SuitJacket` class should behave.
```Python
jacket_one = SuitJacket('Blazer', 0, 2)
jacket_two = SuitJacket('Tuxedo', 2) # number of buttons defaults to 3

jacket_one.get_type() # returns 'Blazer'
jacket_two.get_style_score() # returns 5, number of vents + number of buttons
```

## Closet
Write a `Closet` class that contains `SuitJackets` and can rank them based
on how good the jackets are.

The constructor of `Closet` should take a `List` of `SuitJacket`s and store
them in a data structure of your choice, but it should have the following
methods:
1. `get_jackets_of_type(type)`
  * This method should take in a `String` parameter representing a type
    and return a `List` of all the `SuitJacket`s that have a type
    matching the given `type`. If there are no jackets of that type,
    this method should return an empty `List`.
  * The `SuitJacket`s should be in the same
    order that they were passed into the constructor of the `Closet`.
  * If there are no `SuitJacket`s in the `Closet`, this method should
    return an empty `List`.
2. `get_jackets_by_style()`
  * This method should return a `List` of all the `SuitJacket`s in the,
    `Closet`, ordered by each jacket's overall style. The style is defined
    as the individual `SuitJacket`'s style score, divided by the number of
    jackets that have the same type as that particular `SuitJacket`.
  * The `SuitJacket` with the highest overall style should be at the 'front'
    of the returned `List` (at index 0)
  * If there are no `SuitJacket`s in this `Closet`, should return an empty
    `List`.
3. `add_jacket(jacket)`
  * This method should add the given `SuitJacket` to the `Closet`.
  * For this method, you may assume that the parameter passed will always
    be of type `SuitJacket` and that it will not be `None`.

For Example:
```Python
jacket_one = SuitJacket('Tweed', 1, 2) # get_style_score returns 3
jacket_two = SuitJacket('Tuxedo', 0) # get_style_score returns 3
jacket_three = SuitJacket('Tuxedo', 2, 2) # get_style_score returns 4
closet = Closet([jacket_one, jacket_two, jacket_three])
closet.get_suits_by_style() # [jacket_one, jacket_three, jacket_two]
jacket_four = SuitJacket('Tuxedo', 1)
closet.add_jacket(jacket_four)
closet.get_suits_of_type('Tuxedo') # [jacket_two, jacket_three, jacket_four]
```
In the last function, `jacket_one` has a style score of 3, but there is only 1
`Tweed` jacket, so its overall 'style' is a 3. `jacket_two` also has a style
score of 3, but there are two `Tuxedo` jackets, so it's style is 1.5.
`jacket_three` has a score of 4 / 2, so it is ranked above `jacket_two` but
below `jacket_one`.