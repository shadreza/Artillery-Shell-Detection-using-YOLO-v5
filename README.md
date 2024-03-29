# Artillery Shell Detection using YOLO-v5

The Desktop app works on live and recorded videos and on them it detects the missiles or shells based on the custom trained model via **YOLO-v5** and the predicted object is then tracked live and we can also get the path of the flight even the future predicted flight path of the projectile in 3d. This will eventually show us the hit point of the missile or shell and we can get a rough estimation of the hit point relative coordinates. Also using the **Optical Flow** technology we have been able to detect whether the shell burst or is a blind one also.

### Flow of the work
- Open the Desktop app
- Attach live camera [we used Hero GoPro 10] for live feed or take the recorded video
- Run YOLO on the video or live cam
- Get the results 
- See the projectile in 3d and get to see the burst or blind status

### Accomplished - https://dl.acm.org/doi/10.1145/3582177.3582180

"Tracking of Artillery Shells Using Optical Flow" was the title of my debut conference paper, presented in Macau, China.

IPMV '23: Proceedings of the 2023 5th International Conference on Image Processing and Machine Vision
January 2023
Pages 12–17
