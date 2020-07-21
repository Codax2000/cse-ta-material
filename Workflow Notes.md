# Nailing the CSE 163 Homework

### Alex

## Intro

In my experience, the performance of students in this class has less to do
with their interest, experience, or prior knowledge as their ability to
learn systematically and keep on top of their work. This can be summed up
very simply: not getting behind. This is most commonly shown in the homework,
which students often leave until the last minute, resulting in work that
is not representative of their knowledge. Read on for my advice to
how to work through a homework assignment more systematically, so that
you can worry less about turning it in on time and more about getting it done
right.

## Mindset

Your mindset going in to a homework should be one of plenty - in other words,
don't worry about getting something wrong. Instead, see it as an opportunity
to show off what you know and deepend your understanding of some very cool
material.

## Workflow

I have always done my best work when I stick to a very simple plan. For
any homework assignment, I try to follow this pattern:

1. Start early
2. Read the spec twice before writing code
3. Write function headers and comments
4. Write the testing file
5. Write pseudocode if necessary
6. Write assignment code
7. Run my testing file and debug
   Steps 1-3 don't take long, and are best when done together.
8. Go through the testing file and code with the Style Guide in hand, and run
   flake8.

### Start Early

This is the most critical: whenever you receive an assignment, sit down
with a cup of coffee as soon as you can (no later than the same evening),
read the spec, and start to plan. This allows you to be thinking and planning
how to do it during the week, even if you aren't actively working on it.

### Read the Spec Twice Before Writing Code

This is important because it forces you to examine everything before actually
doing anything. It's another step towards planning, so that once you
do write production code, it goes more quickly.

### Write Function Headers and Comments

This allows you to see the high-level summary of your code, to see if any
functions work together. More importantly, it helps focus on the function
comments, which helps you to understand the behavior of your code. You will
likely forget less special cases and have a better idea of what you are doing
once you write code.

### Write Your Testing File

The reason to do this before writing code is that it causes you to write tests
that are unbiased - in other words, you don't just write them to pass, you
write them to catch bugs in your program. We make this requirement to help
you catch bugs in your own code. Write the best testing file you can,
so if it crashes when your program is run, you know that there is something
wrong with your code. Ideally, your testing file is written so that you know
exactly where something is going wrong.

### Write Pseudocode if necessary

In some cases, particularly with HW4, it is very difficult to just write
some functions. In that case, it is often a good idea to jot down the steps
you are considering taking, so that you can break the problem down into smaller
parts. You can then focus on the smaller tasks instead of looking towards a
miasmatic, difficult problem.

### Write Assignment Code

Only after the previous steps are completed should you actually start writing
code. By this point, the hope is that you have a plan going in, so writing
assignment code should go quickly and smoothly.

### Run Your Testing File

Make sure to run this file! We ask you to write it to benefit you and to
catch mistakes in your code. It can't help you if you never run it.

### Meet the style requirements

Run flake8 on all your .py files, then read through the style guide, line by
line, and see if there is anything you have done that the style guide forbids.
A common example is using `camelCase` - it doesn't break your code, but
our style guide explicitly tells you to use `snake_case`, which often trips up
people coming from CSE 143, where `camelCase` is the norm.

## How to Write Good Function Comments

A function comment should cover the behavior of a function. This should include
all the information a potential client could want, without being overly
wordy. It should also not describe how the function accomplishes its task, so
phrases like 'loops over the dataset' or 'accesses the private `age` variable'
don't add anything to the comment. Here is what you should note in the function
comments:

1. The names and types of any parameters
2. Any default parameters and what they default to
3. The behavior of the function - what is it for? This should only take one or two short sentences.
4. What the function returns and anything the client would need to know about it.

- What type is the return?
- What would a client need to know to use the return? (If a `list`, what
  are the items? If a `dict`, what are the keys and values? If a `DataFrame`,
  what's in it?)
- Are there any special cases? These are generally stated in the spec as an 'if'
  statement, such as 'if the parameter `x` is less than 0, returns `None`'.
  Under what circumstances does the function do something different than
  what your above comment says?
- Are there any assumptions you are making about the input parameters?

## How to Write a Phenomenal Testing File

The idea of a testing file is to catch all the ways your function could go wrong.
Therefore, your mindset when testing should be, 'I am trying to break this'. If
you succeed with your testing file, you have accomplished that goal. Towards this
end, you should test all of your functions, with as many special cases as you can
think of. Anything your function comment says, you should test. Here are some ideas:

- Are there any cases where the function returns `None`, `NaN`, or something
  else that is not usual?
- if the function takes some sort of data structure like a `List`, `Dict`, or `DataFrame`,
  what happens if the data structure is empty? What if it has only one value?
  What if it is missing values?

In any case, you should always make sure to stick to what the spec says. We will
usually tell you how many of the spec tests and how many of your own you will need,
and you should always make sure to stick to the spec. Often, the spec tests will
test your function to work in the 'normal' case, so it is up to you to try
and test the edge cases.

Once you have tested all of the edge cases, satisfied the spec by including
spec tests, and met everything in your function comments, you most likely
have a fantastic testing file.

One more note: Make sure to run it! It makes no sense to work on a testing
file without running it. It's like working for an education and then not
walking at graduation: it's a letdown.
