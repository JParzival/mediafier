# mediafier

<p align="center">
  <img src="./images/logo/logo_195.png" hspace="10">
</p>

🔧 LIBRARY UNDER CONSTRUCTION 🔧

Python library that helps with media (image/video) transformation and augmentation for machine learning and artificial vision projects. Enables the user to modify media for different purposes, as increasing a dataset or just changing some properties.

This library is different to many others in the way that wants to **make image and video transformation simple** by one liners, but fully customisable at the same time. Media transformation for everyone.

<br/>

## 🛠️ Installation

To install the library, read the following lines:

### Pip

```
pip install mediafier
```

To uninstall the library, just execute ```pip uninstall mediafier```

<br/>
<br/>

## 🙏 Our Mantras

* Simple is better than complex
* Less Stack Overflow and more high level programming
* Functions have to be self-explanatory
* As customisable as the user wants through parameters

<br/>
<br/>

## 💡 Features

* This library acts as a wrapper of the most important media transformation libraries nowadays, in order to make media transformation easier to perform.
* Supports both image and video transformation.
* Intended to be focused on media transformation and data augmentation.
* In constant growth, accepts community suggestions, issues and PRs.


<br/>
<br/>

## 💻 Code examples

Let's expose some code examples to show how easy it is to perform transformations with this library:

#### Crop an image

```
import cv2
from mediafier.image.cropping import crop


# Load the image with openCV
img = cv2.imread('path/to/image.png')

# Crop the image from the point 100,100 to the point 200,200
finalimg = crop(img, 100, 100, 100, 100)
```

#### Crop an image keeping original size (by adding borders)

```
import cv2
from mediafier.image.cropping import crop

# Load the image with openCV
img = cv2.imread('path/to/image.png')

# Crop the image from the point 100,100 to the point 200,200
finalimg = crop(img, 100, 100, 100, 100, fill=True)
```

#### Resize an image to the 125% of its size

```
import cv2
from mediafier.image.size import resize

# Load the image with openCV
img = cv2.imread('path/to/image.png')

# Resize the image
finalimg = resize(img, ratio=125)
```

#### Resize an image to 1280x720 changing the interpolation to 'area'

```
import cv2
from mediafier.image.size import resize

# Load the image with openCV
img = cv2.imread('path/to/image.png')

# Resize the image
finalimg = resize(img, size=(1280,720), interpolation='area')
```

#### Draw a bounding box on the image

```
import cv2
from mediafier.image.draw import drawBBox

# Load the image with openCV
img = cv2.imread('path/to/image.png')

# Draw a bounding box from the point 100,100 to the 300,300
finalimg = drawBBox(img, 100, 100, 200, 200, color='black', thickness='2')
```

<br/>
<br/>

## ✨ Contribute

As this is an open-source project it is open to contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas. 

The issues tab is completely open, so don't hesitate posting if you have any issue or you can solve some.

Also, feel free to make pull requests to the project. Creating such a big library requires many hands helping, so help is appreciated!

If you want to make a PR, please follow these steps:

* Create, in the issues tab, a new bug or enhancement.
* In the issue, propose yourself to enhace the solution.
* Prepare the code for that enhancement. Before sending the PR, make sure you are running the latest code and everything works fine. Finally, send the PR following this structure:
  ```
  <what you have done> (fix/closes #<number of the issue>)
  ```
* Wait for it to be published :)

<br/>
<br/>

## 💼 Main contributors

<table>
  <tr>
    <td align="center">
      <a href="" title="Author">👑</a>
      <a href="" title="Reviews the Project">👀</a>
      <a href="" title="Developer">🔧</a>
      <a href="" title="Mantains the project">🚧</a>
      <a href="" title="Answering Questions">💬</a>
      <a href="" title="Makes media">🎨</a> 
      <a href="" title="Documentation">📖</a>
      <br/>
      <a href="https://www.jparzival.com">
        <img src="https://avatars.githubusercontent.com/u/33935947?v=4" width="150px;" alt="JParzival"/><br/>
        <sub><b>Jorge de Andrés</b></sub>
      </a>
      <br/>
      <a href='https://linkedin.com/in/jorgedeandres97'>
        <img src='https://image.flaticon.com/icons/png/512/174/174857.png', width="15px;">
      </a>
      <a href='https://github.com/JParzival'>
        <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png', width="15px;">
      </a>
      <a href='https://open.spotify.com/user/jorgetenisman?si=4c2473495361400f'>
        <img src='https://c0.klipartz.com/pngpicture/67/313/gratis-png-spotify-podcast-spotify-logo.png', width="18px;">
      </a>
    </td>
  </tr>
</table>

<br/>
<br/>

## 📝 Citations

If you are going to cite this project in your scientific publication, please, use the following piece of text to make the citation:

```
@misc{mediafier,
    author = {Jorge de Andres Gonzalez},
    title = {mediafier - A library for image/video transformation and data augmentation},
    year = {2021},
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/JParzival/mediafier}},
}
```
