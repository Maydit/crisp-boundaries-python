# crisp-boundaries-python
Python Implementation of https://github.com/phillipi/crisp-boundaries

Crisp Boundary Detection using Pointwise Mutual Information!!!!

This is far from done. I'm not sure everything is working how it should. 

I tried to implement this for a school project when I couldn't figure out how to run the matlab code and got about partway through. Here's where I left off: learnP_A_B, sampleF, orderAB, getLocalPairs, and extractF are pretty much fully working. I could not figure out how to do the marginalization within evalPMI. For the joint PDF I used a multivariate gaussian kde, which is probably the problem. For the random forest I used a RandomForestClassifier, which should be pretty close. I haven't done the borderSuppress method either. I haven't implemented the getFeatures fully and I'm not sure I'm doing the variance calculation correctly. I genuinely hope that someone can use this code and if you just want to run the original matlab code and couldn't figure it out like me here's how that works: Clone my fork of the repo, install matlab, then compile. The problem was that some features were depreciated which made it error out and show the wrong error message. Also have a great day!
