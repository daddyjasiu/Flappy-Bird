# Flappy Bird - my way of learning Python
 
So I have decided to make a Flappy Bird copy in Python 3.9 using pygame 2.0 library. I want this README to be kind of a blog post so that I can show you the steps I took while developing this game. Now to begin with...

### 1) Background and floor
I've added a static background and scaled it up by `2x`. That is my main surface. The floor is another surface and it is moving. I've done that by placing two floor surfaces next to each other, moving them to the left and then shifting the first one after the second one when the first one is off the screen so that it looks like the whole image is moving and the scene is going in the right direction. 

<p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/1.png?raw=true">
</p>


### 2) Bird
The bird is an another surface, split into three states called `bird_frames`. It contains of 3 frames and the game cycles through them so that the bird seems to be flying - simple animation. I have also added gravity - bird's `x` axis is static, but `y` axis is decreasing with every tick, so the bird is falling down if we aren't pressing space (space = fly up). The bird is also rotating while falling down or flying up using `rotozoom`.
