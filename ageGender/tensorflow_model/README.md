Script and Checkpoints from "Age/Gender detection in TensorFlow"
https://github.com/dpressel/rude-carnie

#### Prediction with fine-tuned inception model

Age Guess:
```
$ python guess.py --model_type inception --model_dir /data/xdata/rude-carnie/checkpoints/age/inception/22801 --filename /Users/yutay/Downloads/portraits/m-60.jpg

```

Gender Guess:
```
$ python guess.py --class_type gender --model_type inception --model_dir /data/xdata/rude-carnie/checkpoints/gender/inception/21936/ --filename /Users/dpressel/Downloads/portraits/m-60.jpg