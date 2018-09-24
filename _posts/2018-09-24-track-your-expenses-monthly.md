---
comments: false
date: 2018-09-24
layout: post
permalink: /2018/09/track-your-expenses-monthly
title: Track your expenses monthly
tags:
- money
- fire
- saving
- tracking
---

This is the second in a series of posts on money management. The first post was [Track your money yearly](/2018/09/track-your-money-yearly).

I'm going to explain how I track my expenses and the spreadsheet I use to do it.
I've added a worksheet called "Expenses Monthly" to the [example money tracking spreadsheet](https://docs.google.com/spreadsheets/d/1dl0V9v8LMHQSDsIbMecp_BC7tyefTuwBziO-ZEyZwsk) I used in my first post. If you haven't done so yet, feel free to make a copy and fill it out. I put in a month of made up example data for you. Over many future posts I'll be extending this example document but for now this post is about the "Expenses Monthly" sheet. If you already have a copy of my spreadsheet from the first post, you can click on the little down arrow on this new worksheet and select "Copy to.." to add this to your sheet.

Here's what it look likes.
![Monthly Expenses worksheet header](/assets/images/moneyMonthlyHeader.png)

## TL;DR

Every month copy over the amount due from your credit card bills and add notes for anything over $150.
You don't even need to do this every month if you don't want, every quarter or so is just fine as well.

Over the years this will become very useful data and allow you to see where your money goes and help you identify patterns and places where you can reduce your expenses.

## Long version

I've read a few financial planning and retire early books and blogs and luckily I was in a pretty good spot before I really started reading up on this. I could never quite get behind a "track absolutely everything" plan because it seemed like too much work. The way I do it is about as much time as I want to put into it while still giving me the benefit I'm looking for (where is my money going).

You're not going to capture absolutely everything on this. Debit card expenses are harder to track and I mostly just skip those.

After a while you can start pre-filling in the regular larly expenses like car insurance, property taxes, school tuition and it really helps you plan out the year.

I much prefer this method than any kind of automated system. First, an automated system involves giving YNAB or whatever you're using your username and password, which means you're really spreading out the security risk of your accounts. Plus to use them you'll likely have to turn off 2 factor authentication which you should for sure be using.

With this approach, you're actually looking at your bills every month and seeing the charges and seeing what you're spending your money on.

Doing this will also help you see that every month is a special month and come to terms with that and it'll really help you plan for your expenses in the future. When I started I had one impression of how much my monthly expenses were and every month I thought, "well this month was a little bit more because of the vet bill", the next month it was the car maintenance and then it was a trip we took and then a broken collarbone. When you see it happening month after month you'll realize how much your expenses really are.

I'll have another post soon on some of the ways I've savd money over the years.

## Columns in the Monthly Expenses worksheet.

Here's all the columns and what to do with them.

###  Month

The month we're talking about. Just set the top one to when you want to start tracking and the rest will magically update.

###  Credit card columns

For each credit card you use, have a column and put in the monthly bill amount every month. Or update it every quarter or as often as you like.

###  Other

This is where I put in expenses that come out of my bank account, things like property taxes, school tuition, paying contractors, ATM withdrawls, anything that isn't on a credit card.

###  Notes

Anything that's over $150 gets mentioned here. It really helps you understand why the bills were high that month.

###  Net Worth

Another post will be coming along about this one too. But if it's easy to work out throw that number in here every month.

###  Gains

For funsies, see how much it changed every month rather than waiting to track it [every year](/2018/09/track-your-money-yearly).

## Spreadsheet Magic

Here's some quick notes on some of the Google Sheets tricks I used.

As usual I delete the unused rows and columns from my sheets. it reduces the chances of my scrolling away from the interesting stuff and it's super easy to add rows and columns when I need them.

`0.0,` I use this format for the numbers to show the values in thousands of dollars with one decimal place. it was too clunky to prefix with a `$` and add `K` at then end so I just skipped them.

`=MOD(INT(YEAR($A:$A)), 2) = 0` this formula for conditional formatting over the whole worksheet gives alternating years a different background

`=EDATE(A2, 1)` an easy way to add a month so that the months all increment. I also chose a date format that had the short month name and year displayed.

`=IF(F3 = "", "", IFERROR(F3 - F2, ""))` for gains to only show a value if we have one.
