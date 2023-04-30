Dynamic Ad Placement


This is my AI Project for dynamic advertisement placemenmt.

Suppose there is an international event going on and there are billboards placed where advertisements are displayed, then it would make more sense if the ads are relevant. That is the product which is available in India but not in US then it would not be proper to display to display the indian product in US. Instead we can display dynamic ads based on the region.

This project is for that purpose only.

First we feed the input to our YOLO model, after a billboard is detected the boundary box coordinates are extracted and then the ad image is resized to the the boundary box aspect ratio, we then put the morphed ad image over the original image thus displaying the ad.

TODO:

There are slight errors in some cases so need to fix that
In some photos the x and y positions switch
Need to implement in live video

Youtube Video: https://youtu.be/Mg89DFmzwUY
