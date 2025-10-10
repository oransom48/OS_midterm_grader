# Manual: how to use these code?
guide for VS code

## Convert grayscale image to 1-bit black & white image using `error_diffusion.py`

1.	put error_diffusion.py and a grayscale image in the same directory
  ``` bash
 	⊢ folder
      ⊢ error_diffusion.py
   	  ∟ input_image_name.png
  ```
2.	click ▷ (Run Python File) at the top right of the window to activate conda
3.	at the terminal, type `python error_diffusion.py <input_image_name.png> <output_image_name.png>`
4.	after the program finished, output_image_name.png must appear in the same directory
  ``` bash
 	⊢ folder
        ⊢ error_diffusion.py
      ∟ input_image_name.png
  ```

## Compare 2 1-bit black & white images using `bw_similarity.py`

1.	put bw_similarity.py and 2 1-bits black & white images in the same directory
  ``` bash
 	⊢ folder
      ⊢ bw_similarity.py
   	  ⊢ bw_image1.png
		  ∟ bw_image2.png
  ```
2.	click ▷ (Run Python File) at the top right of the window to activate conda
3.	at the terminal, type `python bw_similarity.py <bw_image1.png> <bw_image2.png>`
4.	the program will show a new window, which tell you how similar between 2 images are.

> fighting! :)
