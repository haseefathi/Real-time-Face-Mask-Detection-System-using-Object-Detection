# Real-time-Face-Mask-Detection-System-using-Object-Detection

Kaggle Dataset: https://www.kaggle.com/datasets/wobotintelligence/face-mask-detection-dataset

### Description

<ul>
<li>Used Kaggle dataset to train model to detect face masks real-time using TensorFlow and OpenCV. </li>
<li>Finetuned pretrained MobileNet SSD model for face mask detection on ~2000 images and achieved training loss of 0.07 and test loss of 0.11 after 5000 steps. </li>
<li>Utilized Twilio API to convert system to an alert system that sends messages when faces without masks are detected. </li>
</ul>

### Screenshots

#### Single person

| ![With Mask](/screenshots/with.png) | ![Without Mask](/screenshots/without1.png) | ![Without Mask](/screenshots/without2.png) |
| ----------------------------------- | ------------------------------------------ | ------------------------------------------ |

#### Multiple people

![People walking](/screenshots/video.png)
