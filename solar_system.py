import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "SUN",
    (40,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.7,
    (255,255,255),
)

cv2.putText(
    img,
    "Mercury",
    (120,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,255),
)

cv2.putText(
    img,
    "Venus",
    (190,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Earth",
    (280,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Mars",
    (380,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Jupiter",
    (580,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Saturn",
    (740,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Uranus",
    (960,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.putText(
    img,
    "Neptune",
    (1100,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255),
)

cv2.imshow("output",img)
cv2.waitKey(0)

