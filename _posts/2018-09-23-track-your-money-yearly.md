---
comments: false
date: 2018-09-23
layout: post
permalink: /2018/09/track-your-money-yearly
title: Track your money yearly
tags:
- money
- fire
- saving
- tracking
---

This is the first in a series of Money Management posts I plan to make.

I'm going to explain how I track my money and the spreadsheet I use to do it.
I've prepared an [example money tracking spreadsheet](https://docs.google.com/spreadsheets/d/1dl0V9v8LMHQSDsIbMecp_BC7tyefTuwBziO-ZEyZwsk) for you to copy and fill out. I put in one year's worth of made up example data for you. Over many future posts I'll be extending this example document but for now this post is about the "Yearly" worksheet.

Here's what it look likes.
![Yearly worksheet header](/assets/images/moneyYearlyHeader.png)

## TL;DR

Every year when you do your taxes fill out the row for that year with your income and how much taxes you paid.

Over the years this will become very useful data and allow you to see how far you've come over the years and help motivate you to save more and more.

## Columns in the Yearly Worksheet.

Here's all the columns and what to do with them.

###  Year

um, the year. Just change the first year and the rest will adjust automagically.

###  Expenses

Don't worry about this for now, I'll be posting about that in a future post. This'll keep track of how much you actually spend during a given year.

###  AGI

Adjusted Gross Income. From your tax return. This is the biggest number and represents all your income for the year.

###  AMT

Alternative Minimum Tax. Hopefully at some point you're making so much money you end up paying this. Some of it you can claw back in future years. It's complicated.

###  Fed Tax

How much federal tax you paid.

###  State Tax

How much federal tax you paid. If you pay taxes in multiple states you could add more columns, or just add them all up into one column.

###  Effective Tax rate

How much of your AGI was used to pay taxes. This number should be less than you expect and various strategies
can help you lower it. This is something I wish I'd tracked sooner.

###  Net Worth

Another post will be coming along about this one too. But if it's easy to work out throw that number in here.

###  me & spouse

These columns are for you to add life events into. Mostly events realted to your financial planning. Like when you can withdraw from your retirement plans, when you should collect social security, sign up for medicare etc.

![Yearly worksheet notes](/assets/images/moneyYearlyNotes.png)

###  Notes

I use this as a freeform column to add notes about the year. Mostly what were some of the biggest expenses or what might explain large income. E.G. sold stock, bought new car, remodelled kitchen.

## Spreadsheet Magic

Here's some quick notes on some of the Google Sheets tricks I used.

`=$A3 + 1` is how I auto increment the year from one row to the next. $A$3 is the starting year, everything works off the previous row. I entered this forula in $A$4, hit enter, copied it and then selected the rest of the A cells and pasted in the value. Google Sheets increments the row number for every row so you'll always be adding one to the previous row.

Using `$` is how you tell sheets not to auto increment that reference when you copy paste to another row or column.

`"$"0,"K"` and `"$"0.0,,"M"` is how I format numbers to be in the thousands (or millions).

`=IFERROR((E5 + F5) / C5, "")` on the Effective Tax Rate column avoids showing an error if values are missing. This way the column only fills out if you have an AGI and Tax columns filled out.

`=MOD(INT($A:$A / 10), 2) > 0` I use this with conditional formatting to get blocks of 10 years to alternate colors. This helps me gauge the passing of time without having to deal with border lines in the worksheet.

`=IFERROR(SUM(FILTER('Expenses Monthly'!B:D , YEAR('Expenses Monthly'!A:A) = $A3)), "")` I don't use it in this example yet, but it's coming. This is how I sum up some numbers from a different worksheet in the same Google Spreadsheet.
