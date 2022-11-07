# DDOS (Distributed Denial of Service) Incident Report

## Duration:

- The unavailability of our website was caused by the attack 
that started at 8:00 am. We managed to fix it on 6th Jan 2022 to 7th the 
next day at 5:00am through some upgrades.

## Impact

- The attacks caused the website data to be unavailable 
which prevented the users who used browsers since it 
overwhelmed the servers by continuously fetching  the website 
resources in an endless continuous loop.

- It didn’t affect the mobile or desktop applications users much 
although after some research some said that uploading photos was slower than the other times.

## Root cause

The attack was caused by a software created and redirected to users who 
visited some website that we believed was a scam trying to imitate our services.
It was created by a hacker and was launched after he/she was convicted that most users were online.
The users’ devices continuously sent many requests and the 
servers could not handle all those and still serve static and dynamic content easily.

## Timeline

- The attack happened on Jan 6th 2022 8:00 am.

- We were launching new features on that day and realized that something was wrong.
Some users called us claiming the unavailability of the website, they said it took long to load and the app(both desktop and mobile users
claimed that uploading photos took longer than usual.

- We checked if the clusters(all of them were functioning) plus the software(applications) running on them. We also bought more virtual machines immediately 
to increase the scale since we thought we had  a sharp rise in users.

- The only misleading investigation we did was asking users from different locations whether the website worked on their side.
This should have been obvious since if it didn't work on our side it couldn't on theirs.

- The issue required a backend security upgrade. 
It was handed over to the Cloud compute engineers to 
add some logic which could detect excessive requests from a single user and whether those requests were in a short while.
We also did some security awareness campaigns to warn against false websites which could cause threats in the future.

- To solve the issue, we announced a *downtime* and the *reconnection time* to warn __users__ and 
shutted down the servers, updated our Software to 
handle multiple requests and block excessive(DDOS) requests 
and embedded a security upgrade in our website. 
We restarted our servers on the announced time and also did some tests which were a success.

