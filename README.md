# Flappy Bird - my way of learning Python
 
 <p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/run.gif?raw=true">
</p>
 
So I have decided to make a Flappy Bird copy in Python 3.9 using pygame 2.0 library. I want this README to be kind of a blog post so that I can show you the steps I took while developing this game. Now to begin with...

### 1) Background and floor
I've added a static background and scaled it up by `2x`. That is my main surface. The floor is another surface and it is moving. I've done that by placing two floor surfaces next to each other, moving them to the left and then shifting the first one after the second one when the first one is off the screen so that it looks like the whole image is moving and the scene is going in the right direction. 

<p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/1.png?raw=true">
</p>


### 2) Bird
The bird is an another surface, split into three states called `bird_frames`. It contains of 3 frames and the game cycles through them so that the bird seems to be flying - simple animation. I have also added `gravity` - bird's `x` axis is static, but `y` axis is decreasing with every tick, so the bird is falling down if we aren't pressing space (space = fly up). The bird is also rotating while falling down or flying up using `rotozoom`.

<p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/2.png?raw=true">
</p>


### 3) Pipes
Creating pipes was actually not that easy. The bird has to fly between two pipes: one being bottom pipe and second being top pipe. They have to spawn at random heights so that the game is more challenging. I started by importing pipe surface, creating `USEREVENT` which helps me with spawning them and writing three functions: `create_pipe`, `draw_pipes` and `move_pipes`. The first one basically randomizes the height of each pipe and assigns it to their `Y` value. The second function draws pipes on the screen (if pipe is `<1024` then flip the pipe vertically, because we need one pipe facing down and one pipe facing up). Last function moves pipes to the left - pretty straightforward.

<p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/4.png?raw=true">
</p>


### 4) Score system, game over screen and sounds
Player scores a point whenever he passes through pipes. Because the game runs pretty fast, I had to add another condition to scoring a point which is: previous pipe (one already scored) has to be off screen (so basically it's `x` value has to be `<0`). With that, the points are calculated correctly, one by one. High score is also calculated for each run. 

Score and high score are always shown after player loses. I have used original FB font called `04B_19` for output and I have also put `game_over` image so it looks good after lose.

Every time player flies up, the bird flaps its wings and makes a `flap_sound`. When scoring point, you can hear `score_sound` and if you die, you hear `death_sound`.

<p align="center">
  <img width = "186" height = "328" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/5.png?raw=true">
</p>

### 5) Collisions
You may be wondering how I calculate collisions - it's actually quite simple. In `pygame` there is a thing called `rect` that basically puts a rectangle around a surface. I've put `rects` around `bird_surface` and `pipe_surface`, and if these rectangles touch each other, player loses. It is not the best way to calculate and resolve collisions, but for out sprites and movement, it works quite well. In addition, player loses if bird touches the ground or flies too high. `Blue` colour below is to represent the `rects` and `red` is the collision of the bird and pipe resulting in player's loss.

<p align="center">
  <img width = "348" height = "234" src="https://github.com/hi-im-happy/Flappy-Bird/blob/main/img/6.png?raw=true">
</p>

### 6) Optimization
After testing the game for any bugs I've noticed that the longer we play, the slower the game gets. I've noticed, that it is because the pipes were generating infinitely and were just left behind as we progressed further in game. I fixed that by detecting pipes that are already off screen, and drawing only these, that are not with this line of code: 

```    
visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
return visible_pipes
```

## ...and done!
The game is playable, everything is working properly. I've really enjoyed this project and I'm looking forward to developing something new using `pygame` in `Python`.
