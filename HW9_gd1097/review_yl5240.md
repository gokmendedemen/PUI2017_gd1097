<img width="658" alt="hw8_yl5240_3" src="https://user-images.githubusercontent.com/31747292/32961353-3850322c-cb96-11e7-895d-8aeffd8a8a85.png">

## Five borough's median values of the census tracts' income and house value in 2010, based on ACS data


Review by Gokmen Dedemen (gd1097): 

**In terms of clarity**, I think it is easy to understand the figure, overall. However, the issues regarding clarity are the followings: Writing the population inside the circles is a good idea. However, the size of the text is also getting smaller or larger proportional to population (size of circles). This makes, for instance, the text written in Staten Islands circle (466k) really small, and harder to read. I think it is better to keep text sizes constant. If they do not fit into the circles, maybe they can be written outside of the circles. **In terms of esthetic**, I checked the plot using color blindless simulator (http://www.color-blindness.com/coblis-color-blindness-simulator/). When I use Red-Blind/Protanopia filter, I noticed that Queens and Manhattan looks like similar. The same issue applies for Bronx and Brooklyn. I recommend that the colors should be changed to avoid confusion for color blinded people. **In terms of honesty**, if we check the scales in x and y axes, we notice that a 10 k ($) difference in the x axis is represented by almost the same distance that corresponds 100 k ($) difference in y axis. This problem arises since the units of both x and y axis are the same ($). That's why I would expect to see not only proportional distances in the xticks and yticks labels, seperately, but I would also expect to see that distances between both x and y ticks labels are proportional. In other words, a 100 k difference in y axes should have been represented by a distance 10 times larger than the distance used in x axes representing 10 k difference. Therefore, I would say this plot has a high lie factor that needs to be taken care off, and it does not honestly reproduce data. 

# FBB very good. 
also why are the points in the legend in different size? if they reflect the overall borough population that is redundant with the plot. otherwise it is confusing
