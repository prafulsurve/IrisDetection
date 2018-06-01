# IrisDetection

Detects the iris region from the input image. Saves the iris image on local path and performs the normalization process by Daugman’s rubber sheet model.

## Normalization
Normalization step transforms the circular iris region in a fixed dimension so that the iris scanning and comparison step becomes efficient. Daugman’s rubber sheet model which can be used as a normalization step. Daugman’s rubber sheet model realizes the iris circle in a polar coordinates (r, θ) and normalizes it in cartesian co-ordinates.
