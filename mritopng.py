import os
import png
import dicom


def mri_to_png(mri_file_path, png_file_path):
	""" Function to convert an MRI binary file to a
		PNG image file.

		@param mri_file_path: Full path to the mri file
		@param png_file_path: Fill path to the png file
	"""

	# Extracting data from the mri file
	plan = dicom.read_file(mri_file_path)
	shape = plan.pixel_array.shape

	image_2d = []
	max_val = 0
	for row in plan.pixel_array:
		pixels = []
		for col in row:
			pixels.append(col)
			if col > max_val: max_val = col
		image_2d.append(pixels)

	# Rescalling greyscale between 0-255
	image_2d_scaled = []
	for row in image_2d:
		row_scaled = []
		for col in row:
			col_scaled = int((float(col)/float(max_val))*255.0)
			row_scaled.append(col_scaled)
		image_2d_scaled.append(row_scaled)

	# Writing the PNG file
	f = open(png_file_path, 'wb')
	w = png.Writer(shape[0], shape[1], greyscale=True)
	w.write(f, image_2d_scaled)
	f.close()


def convert_folder(mri_folder, png_folder):
	""" Convert all MRI files in a folder to png files
		in a destinaiton folder
	"""
	os.makedirs(png_folder)
	for mri_file in os.listdir(mri_folder):
		mri_file_path = os.path.join(mri_folder, mri_file)
		png_file_path = os.path.join(png_folder, '%s.png' % mri_file)
		try:
			mri_to_png(mri_file_path, png_file_path)
			print mri_file_path, '-->', png_file_path
		except:
			print 'FAIL>', mri_file_path, '-->', png_file_path
