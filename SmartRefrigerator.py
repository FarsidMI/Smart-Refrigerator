{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Oblique;}
{\colortbl;\red255\green255\blue255;\red0\green29\blue164;\red9\green9\blue9;\red121\green121\blue121;
\red17\green109\blue18;\red18\green51\blue230;\red2\green34\blue149;}
{\*\expandedcolortbl;;\csgenericrgb\c0\c11373\c64314;\csgenericrgb\c3529\c3529\c3529;\csgenericrgb\c47451\c47451\c47451;
\csgenericrgb\c6667\c42745\c7059;\csgenericrgb\c7059\c20000\c90196;\csgenericrgb\c784\c13333\c58431;}
\margl1440\margr1440\vieww13440\viewh7240\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 import \cf3 json\
\cf2 import \cf3 os\
\cf2 import \cf3 sys\
\cf2 import \cf3 time\
\cf2 import \cf3 cv2\
\cf2 import \cf3 discord \cf2 as \cf3 discord\
\cf2 import \cf3 numpy \cf2 as \cf3 np\
\cf2 import \cf3 requests\
\cf2 import \cf3 tensorflow \cf2 as \cf3 tf\
\cf2 from \cf3 discordwebhook \cf2 import \cf3 Discord\
\cf2 from \cf3 twilio.rest \cf2 import \cf3 Client\
\

\f1\i \cf4 # Replace the placeholders with your Twilio account SID, auth token, and phone numbers\
\

\f0\i0 \cf3 account_sid = \cf5 'AC37e5afca9c6c292d254d79824sc2cb486'\
\cf3 auth_token = \cf5 '9c72d332bf36a3e1fb46b7sac9d115aff'\
\cf3 twilio_phone_number = \cf5 '+14345954350'\
\cf3 recipient_phone_number = \cf5 '+1'\
\

\f1\i \cf4 # using discord as a way to notify user\

\f0\i0 \cf3 discord = Discord(\
    url=\cf5 "https://discord.com/api/webhooks/1090800548594339930/DXEsmaf_F3CHllCPHymvgmChD5vEzNMgenp9R0sXyQesx2ENP5tdvSVTQgvFFIh8eJPrd"\cf3 )\
\

\f1\i \cf4 # writes typ-writer style messages on the console UI\

\f0\i0 \cf2 def \cf3 write(message):\
\
    \cf2 for \cf3 char \cf2 in \cf3 message:\
        sys.stdout.write(char)\
        sys.stdout.flush()\
        time.sleep(\cf6 0.05\cf3 )\
\

\f1\i \cf4 # initial scan of the fridge (full image) -> 'FRIDGE' folder\

\f0\i0 \cf2 def \cf3 pic0():\
    
\f1\i \cf4 # Create a VideoCapture object to access the webcam\
    
\f0\i0 \cf3 cap = cv2.VideoCapture(\cf6 0\cf3 )\
    
\f1\i \cf4 # Check if the webcam is opened successfully\
    
\f0\i0 \cf2 if not \cf3 cap.isOpened():\
        print(\cf5 "Could not open webcam"\cf3 )\
        exit()\
\
    
\f1\i \cf4 # Add a delay to allow the camera to adjust the shutter\
    
\f0\i0 \cf3 time.sleep(\cf6 2\cf3 )\
\
    
\f1\i \cf4 # Read a frame from the webcam\
    
\f0\i0 \cf3 ret, frame = cap.read()\
    
\f1\i \cf4 # Release the VideoCapture object\
    
\f0\i0 \cf3 cap.release()\
    
\f1\i \cf4 # Check if the frame is captured successfully\
    
\f0\i0 \cf2 if not \cf3 ret:\
        print(\cf5 "Could not capture frame"\cf3 )\
        exit()\
    
\f1\i \cf4 # Adjust brightness and contrast\
    #alpha = 1.5  # Contrast control (1.0-3.0)\
    #beta = 50  # Brightness control (0-100)\
    #frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)\
    # Set the path and filename for the image\
    
\f0\i0 \cf3 folder_path = \cf5 "/home/fruit/CAPSTONE/FRIDGE"\
    \cf3 filename = \cf5 "fridge_image.jpg"\
    \cf3 file_path = os.path.join(folder_path, filename)\
    
\f1\i \cf4 # Save the image\
    
\f0\i0 \cf3 cv2.imwrite(file_path, frame)\
    
\f1\i \cf4 #print(f"Image saved successfully at \{file_path\}")\
    
\f0\i0 \cf3 write(message=\cf5 "\cf7 \\n\cf5 CAPTURE 1: "\cf3 )\
    print(\cf5 "COMPLETE!"\cf3 )\
\
\cf2 def \cf3 pic1():\
    
\f1\i \cf4 # Create a VideoCapture object to access the webcam\
    
\f0\i0 \cf3 cap = cv2.VideoCapture(\cf6 0\cf3 )\
    
\f1\i \cf4 # Check if the webcam is opened successfully\
    
\f0\i0 \cf2 if not \cf3 cap.isOpened():\
        print(\cf5 "Could not open webcam"\cf3 )\
        exit()\
\
    
\f1\i \cf4 # Add a delay to allow the camera to adjust the shutter\
    
\f0\i0 \cf3 time.sleep(\cf6 2\cf3 )\
\
    
\f1\i \cf4 # Read a frame from the webcam\
    
\f0\i0 \cf3 ret, frame = cap.read()\
    
\f1\i \cf4 # Release the VideoCapture object\
    
\f0\i0 \cf3 cap.release()\
    
\f1\i \cf4 # Check if the frame is captured successfully\
    
\f0\i0 \cf2 if not \cf3 ret:\
        print(\cf5 "Could not capture frame"\cf3 )\
        exit()\
    
\f1\i \cf4 # Adjust brightness and contrast\
    #alpha = 1.5  # Contrast control (1.0-3.0)\
    #beta = 50  # Brightness control (0-100)\
    #frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)\
    # Set the path and filename for the image\
    
\f0\i0 \cf3 folder_path = \cf5 "/home/fruit/CAPSTONE/FRIDGE/MAIN_IMG"\
    \cf3 filename = \cf5 "fridge_image.jpg"\
    \cf3 file_path = os.path.join(folder_path, filename)\
    
\f1\i \cf4 # Save the image\
    
\f0\i0 \cf3 cv2.imwrite(file_path, frame)\
    
\f1\i \cf4 #print(f"Image saved successfully at \{file_path\}")\
    
\f0\i0 \cf3 write(message=\cf5 "\cf7 \\n\cf5 CAPTURE 2: "\cf3 )\
    print(\cf5 "COMPLETE!"\cf3 )\
\

\f1\i \cf4 # splits the initial scan into four quadrants (four images) -> 'FRIDGE' folder\

\f0\i0 \cf2 def \cf3 pic4():\
    
\f1\i \cf4 # Create a VideoCapture object to access the webcam\
    
\f0\i0 \cf3 cap = cv2.VideoCapture(\cf6 0\cf3 )\
    
\f1\i \cf4 # Check if the webcam is opened successfully\
    
\f0\i0 \cf2 if not \cf3 cap.isOpened():\
        print(\cf5 "Could not open webcam"\cf3 )\
        exit()\
\
    
\f1\i \cf4 # Add a delay to allow the camera to adjust the shutter\
    
\f0\i0 \cf3 time.sleep(\cf6 1\cf3 )\
\
    
\f1\i \cf4 # Read a frame from the webcam\
    
\f0\i0 \cf3 ret, frame = cap.read()\
    
\f1\i \cf4 # Release the VideoCapture object\
    
\f0\i0 \cf3 cap.release()\
    
\f1\i \cf4 # Check if the frame is captured successfully\
    
\f0\i0 \cf2 if not \cf3 ret:\
        print(\cf5 "Could not capture frame"\cf3 )\
        exit()\
    
\f1\i \cf4 # Adjust brightness and contrast\
    #alpha = 1.5  # Contrast control (1.0-3.0)\
    #beta = 50  # Brightness control (0-100)\
    #frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)\
    # Crop the image into four quadrants\
    
\f0\i0 \cf3 height, width, channels = frame.shape\
    half_height = height // \cf6 2\
    \cf3 half_width = width // \cf6 2\
    \cf3 top_left = frame[\cf6 0\cf3 :half_height, \cf6 0\cf3 :half_width]\
    top_right = frame[\cf6 0\cf3 :half_height, half_width:width]\
    bottom_left = frame[half_height:height, \cf6 0\cf3 :half_width]\
    bottom_right = frame[half_height:height, half_width:width]\
    
\f1\i \cf4 # Set the path and filenames for the images\
    
\f0\i0 \cf3 folder_path = \cf5 "/home/fruit/CAPSTONE/FRIDGE"\
    \cf3 top_left_filename = \cf5 "fridge_image_top_left.jpg"\
    \cf3 top_right_filename = \cf5 "fridge_image_top_right.jpg"\
    \cf3 bottom_left_filename = \cf5 "fridge_image_bottom_left.jpg"\
    \cf3 bottom_right_filename = \cf5 "fridge_image_bottom_right.jpg"\
    \cf3 top_left_path = os.path.join(folder_path, top_left_filename)\
    top_right_path = os.path.join(folder_path, top_right_filename)\
    bottom_left_path = os.path.join(folder_path, bottom_left_filename)\
    bottom_right_path = os.path.join(folder_path, bottom_right_filename)\
    
\f1\i \cf4 # Save the images\
    
\f0\i0 \cf3 cv2.imwrite(top_left_path, top_left)\
    cv2.imwrite(top_right_path, top_right)\
    cv2.imwrite(bottom_left_path, bottom_left)\
    cv2.imwrite(bottom_right_path, bottom_right)\
    
\f1\i \cf4 #print(f"Images saved successfully at \{folder_path\}")\
    
\f0\i0 \cf3 write(message=\cf5 "\cf7 \\n\cf5 CAPTURE 3: "\cf3 )\
    print(\cf5 "COMPLETE!\cf7 \\n\cf5 "\cf3 )\
\

\f1\i \cf4 # tensorflow scans images -> 'FRIDGE' folder -> outputs text file -> 'PREDICTION' folder\

\f0\i0 \cf2 def \cf3 scan():\
    write(message=\cf5 "\cf7 \\n\cf5 ANALYZING CAPTURES WITH TENSORFLOW\cf7 \\n\\n\cf5 "\cf3 )\
    \cf2 global \cf3 output_file_path\
\
    
\f1\i \cf4 # load the pre-trained InceptionV3 model\
    
\f0\i0 \cf3 model = tf.keras.applications.InceptionV3(weights=\cf5 'imagenet'\cf3 )\
\
    
\f1\i \cf4 # set the folder path containing the images to classify\
    
\f0\i0 \cf3 folder_path = \cf5 '/home/fruit/CAPSTONE/FRIDGE'\
\
    
\f1\i \cf4 # set the path to the output text file\
    
\f0\i0 \cf3 output_file_path = \cf5 '/home/fruit/CAPSTONE/PREDICTED/predictions.txt'\
\
    
\f1\i \cf4 # get a list of all the image files in the folder\
    
\f0\i0 \cf3 image_files = [os.path.join(folder_path, f) \cf2 for \cf3 f \cf2 in \cf3 os.listdir(folder_path) \cf2 if\
                   \cf3 f.endswith(\cf5 '.jpg'\cf3 ) \cf2 or \cf3 f.endswith(\cf5 '.jpeg'\cf3 ) \cf2 or \cf3 f.endswith(\cf5 '.png'\cf3 )]\
\
    
\f1\i \cf4 # create an empty set to store unique predicted class labels\
    
\f0\i0 \cf3 unique_predictions = set()\
\
    
\f1\i \cf4 # loop over each image file and classify it\
    
\f0\i0 \cf2 for \cf3 img_path \cf2 in \cf3 image_files:\
        
\f1\i \cf4 # load and preprocess the image\
        
\f0\i0 \cf3 img = tf.keras.preprocessing.image.load_img(img_path, target_size=(\cf6 299\cf3 , \cf6 299\cf3 ))\
        img_array = tf.keras.preprocessing.image.img_to_array(img)\
        img_array = np.expand_dims(img_array, axis=\cf6 0\cf3 )\
        img_array = tf.keras.applications.inception_v3.preprocess_input(img_array)\
\
        
\f1\i \cf4 # use the model to make a prediction on the image\
        
\f0\i0 \cf3 prediction = model.predict(img_array)\
\
        
\f1\i \cf4 # decode the prediction to get the predicted class label\
        
\f0\i0 \cf3 predicted_class = tf.keras.applications.inception_v3.decode_predictions(prediction, top=\cf6 1\cf3 )[\cf6 0\cf3 ][\cf6 0\cf3 ]\
\
        
\f1\i \cf4 # add the predicted class label to the set of unique predictions\
        
\f0\i0 \cf3 unique_predictions.add(predicted_class[\cf6 1\cf3 ].replace(\cf5 '_'\cf3 , \cf5 ' '\cf3 ))\
\
    
\f1\i \cf4 # write the set of unique predicted class labels to a text file\
    
\f0\i0 \cf2 with \cf3 open(output_file_path, \cf5 'w'\cf3 ) \cf2 as \cf3 f:\
        \cf2 for \cf3 prediction \cf2 in \cf3 unique_predictions:\
            f.write(prediction + \cf5 '\cf7 \\n\cf5 '\cf3 )\
\

\f1\i \cf4 # scans the text file + attaches full capture -> discord\

\f0\i0 \cf2 def \cf3 send():\
    discord.post(\
        username=\cf5 "FRIDGE"\cf3 ,\
        content=\cf5 "\cf7 \\n\cf5 ITEMS IN YOUR FRIDGE:\cf7 \\n\\n\cf5 "\cf3 ,\
        avatar_url=\cf5 "https://static.wikia.nocookie.net/adventure-time-facts/images/0/0c/BMO.jpg/revision/latest?cb=20130102063835"\cf3 ,\
\
    )\
\
    file_path = \cf5 '/home/fruit/CAPSTONE/PREDICTED/predictions.txt'\
    
\f1\i \cf4 # Reads the contents within the file saved from Tensorflow\
    
\f0\i0 \cf2 with \cf3 open(file_path, \cf5 'r'\cf3 ) \cf2 as \cf3 f:\
        file_contents = f.read()\
        print(\cf5 "\cf7 \\n\cf5 ITEMS FOUND: \cf7 \\n\cf5 "\cf3 )\
        write(message=file_contents)\
\
    discord.post(\
        username=\cf5 "FRIDGE"\cf3 ,\
        content=file_contents, file=\{\cf5 "file1"\cf3 : open(\cf5 "/home/fruit/CAPSTONE/FRIDGE/MAIN_IMG/fridge_image.jpg"\cf3 , \cf5 "rb"\cf3 )\},\
        avatar_url=\cf5 "https://static.wikia.nocookie.net/adventure-time-facts/images/0/0c/BMO.jpg/revision/latest?cb=20130102063835"\cf3 ,\
\
    )\
\
    write(message=\cf5 "\cf7 \\n\cf5 SUCCESSFULLY SENT LIST TO DISCORD & SMS !\cf7 \\n\cf5 "\cf3 )\
\
\

\f1\i \cf4 # sends scanned text file & sends item list -> SMS text\

\f0\i0 \cf2 def \cf3 sms():\
    file_path = \cf5 '/home/fruit/CAPSTONE/PREDICTED/predictions.txt'\
    
\f1\i \cf4 # Reads the contents within the file saved from Tensorflow\
    
\f0\i0 \cf2 with \cf3 open(file_path, \cf5 'r'\cf3 ) \cf2 as \cf3 f:\
        file_contents = f.read()\
\
    account_sid = \cf5 "AC37e5afca9c6c292d254d79824sc2cb486"\
    \cf3 auth_token = \cf5 "9c72d332bf36a3e1fb46b7ac9d115saff"\
    \cf3 client = Client(account_sid, auth_token)\
    message = client.messages.create(\
        body=\cf5 '\cf7 \\n\\n\cf5 ITEMS IN YOUR FRIDGE:\cf7 \\n\\n\cf5 ' \cf3 + file_contents,\
        from_=\cf5 "+14345954350"\cf3 ,\
        to=\cf5 "+14167286464"\
    \cf3 )\
    print(\cf5 "\cf7 \\n\cf5  "\cf3 )\
    print(message.sid)\
\

\f1\i \cf4 # scans text file with food items and generates nutrition facts per item\

\f0\i0 \cf2 def \cf3 all_facts():\
    
\f1\i \cf4 # set the API endpoint and API key\
    
\f0\i0 \cf3 endpoint = \cf5 "https://api.nal.usda.gov/fdc/v1/search"\
    \cf3 api_key = \cf5 "QpsCiLx41euREJtAnTqeSLyG4X6gMq5SCxVN0tPJX"\
    
\f1\i \cf4 # read the list of food items from a text file\
    
\f0\i0 \cf2 with \cf3 open(\cf5 "/home/fruit/CAPSTONE/PREDICTED/predictions.txt"\cf3 , \cf5 "r"\cf3 ) \cf2 as \cf3 f:\
        foods = f.read().splitlines()\
    
\f1\i \cf4 # loop over each food item and search the API for nutrition facts\
    
\f0\i0 \cf2 for \cf3 food \cf2 in \cf3 foods:\
        params = \{\
            \cf5 "api_key"\cf3 : api_key,\
            \cf5 "generalSearchInput"\cf3 : food,\
            \cf5 "requireAllWords"\cf3 : \cf5 "true"\cf3 ,\
            \cf5 "pageSize"\cf3 : \cf5 "1"\cf3 ,\
            \cf5 "sortField"\cf3 : \cf5 "dataType.keyword"\cf3 ,\
            \cf5 "sortDirection"\cf3 : \cf5 "desc"\
        \cf3 \}\
        response = requests.get(endpoint, params=params).json()\
        \cf2 if \cf3 response[\cf5 "foods"\cf3 ]:\
            item = response[\cf5 "foods"\cf3 ][\cf6 0\cf3 ]\
            nutrients = item[\cf5 "foodNutrients"\cf3 ]\
            print(\cf5 f"Food: \cf7 \{\cf3 item[\cf5 'description'\cf3 ]\cf7 \}\cf5 "\cf3 )\
            \cf2 if \cf5 "servingSize" \cf2 in \cf3 item:\
                print(\cf5 f"Serving Size: \cf7 \{\cf3 item[\cf5 'servingSize'\cf3 ]\cf7 \}\cf5 "\cf3 )\
            \cf2 for \cf3 nutrient \cf2 in \cf3 nutrients:\
                print(\cf5 f"\cf7 \{\cf3 nutrient[\cf5 'nutrientName'\cf3 ]\cf7 \}\cf5 : \cf7 \{\cf3 nutrient[\cf5 'value'\cf3 ]\cf7 \} \{\cf3 nutrient[\cf5 'unitName'\cf3 ]\cf7 \}\cf5 "\cf3 )\
            print()\
        \cf2 else\cf3 :\
            print(\cf5 f"No results found for \cf7 \{\cf3 food\cf7 \}\cf5 "\cf3 )\
\
\
\cf2 def \cf3 facts():\
    
\f1\i \cf4 # set the API endpoint and API key\
    
\f0\i0 \cf3 endpoint = \cf5 "https://api.nal.usda.gov/fdc/v1/search"\
    \cf3 api_key = \cf5 "QpsCiLx41euREJtAnTqeSLyG4X6gMq5SCVN0tPJX"\
    
\f1\i \cf4 # read the list of food items from a text file\
    
\f0\i0 \cf2 with \cf3 open(\cf5 "/home/fruit/CAPSTONE/PREDICTED/predictions.txt"\cf3 , \cf5 "r"\cf3 ) \cf2 as \cf3 f:\
        foods = f.read().splitlines()\
    
\f1\i \cf4 # loop over each food item and search the API for nutrition facts\
    
\f0\i0 \cf2 for \cf3 food \cf2 in \cf3 foods:\
        params = \{\
            \cf5 "api_key"\cf3 : api_key,\
            \cf5 "generalSearchInput"\cf3 : food,\
            \cf5 "requireAllWords"\cf3 : \cf5 "true"\cf3 ,\
            \cf5 "pageSize"\cf3 : \cf5 "1"\cf3 ,\
            \cf5 "sortField"\cf3 : \cf5 "dataType.keyword"\cf3 ,\
            \cf5 "sortDirection"\cf3 : \cf5 "desc"\
        \cf3 \}\
        response = requests.get(endpoint, params=params).json()\
        \cf2 if \cf3 response[\cf5 "foods"\cf3 ]:\
            item = response[\cf5 "foods"\cf3 ][\cf6 0\cf3 ]\
            nutrients = item[\cf5 "foodNutrients"\cf3 ]\
            \cf2 for \cf3 nutrient \cf2 in \cf3 nutrients:\
                \cf2 if \cf3 nutrient[\cf5 'nutrientName'\cf3 ] == \cf5 'Energy'\cf3 :\
                    print(\cf5 f"Food: \cf7 \{\cf3 item[\cf5 'description'\cf3 ]\cf7 \}\cf5 "\cf3 )\
                    \cf2 if \cf5 "servingSize" \cf2 in \cf3 item:\
                        print(\cf5 f"Serving Size: \cf7 \{\cf3 item[\cf5 'servingSize'\cf3 ]\cf7 \}\cf5 "\cf3 )\
                    print(\cf5 f"Calories: \cf7 \{\cf3 nutrient[\cf5 'value'\cf3 ]\cf7 \} \{\cf3 nutrient[\cf5 'unitName'\cf3 ]\cf7 \}\cf5 "\cf3 )\
                    print()\
        \cf2 else\cf3 :\
            print(\cf5 f"No results found for \cf7 \{\cf3 food\cf7 \}\cf5 "\cf3 )\
\

\f1\i \cf4 # determines calories for known food items in the image scan (text file)\

\f0\i0 \cf2 def \cf3 disco_calories():\
    
\f1\i \cf4 # set the API endpoint and API key\
    
\f0\i0 \cf3 endpoint = \cf5 "https://api.nal.usda.gov/fdc/v1/search"\
    \cf3 api_key = \cf5 "QpsCiLx41euREJtAnTqeSLyG4X6gMq5SCVN0tPJX"\
    
\f1\i \cf4 # read the list of food items from a text file\
    
\f0\i0 \cf2 with \cf3 open(\cf5 "/home/fruit/CAPSTONE/PREDICTED/predictions.txt"\cf3 , \cf5 "r"\cf3 ) \cf2 as \cf3 f:\
        foods = f.read().splitlines()\
\
    
\f1\i \cf4 # create the payload to send to Discord\
    
\f0\i0 \cf3 webhook_url = \cf5 'https://discord.com/api/webhooks/1090800488414445618/Wp365OH8RsKNv6WzClHm1CKOpCdSdwFLGmnjgv3Cq4DfEczSWKV0Vh2wgXnb0qKw-jYt'\
    \cf3 payload = \{\}\
\
    
\f1\i \cf4 # loop over each food item and search the API for nutrition facts\
    
\f0\i0 \cf2 for \cf3 food \cf2 in \cf3 foods:\
        params = \{\
            \cf5 "api_key"\cf3 : api_key,\
            \cf5 "generalSearchInput"\cf3 : food,\
            \cf5 "requireAllWords"\cf3 : \cf5 "true"\cf3 ,\
            \cf5 "pageSize"\cf3 : \cf5 "1"\cf3 ,\
            \cf5 "sortField"\cf3 : \cf5 "dataType.keyword"\cf3 ,\
            \cf5 "sortDirection"\cf3 : \cf5 "desc"\
        \cf3 \}\
        response = requests.get(endpoint, params=params).json()\
        \cf2 if \cf3 response[\cf5 "foods"\cf3 ]:\
            item = response[\cf5 "foods"\cf3 ][\cf6 0\cf3 ]\
            nutrients = item[\cf5 "foodNutrients"\cf3 ]\
            food_name = item[\cf5 'description'\cf3 ]\
            payload[\cf5 'content'\cf3 ] = \cf5 f"**Food:** \cf7 \{\cf3 food_name\cf7 \}\\n\cf5 "\
            \cf2 if \cf5 "servingSize" \cf2 in \cf3 item:\
                serving_size = item[\cf5 'servingSize'\cf3 ]\
                payload[\cf5 'content'\cf3 ] += \cf5 f"**Serving Size:** \cf7 \{\cf3 serving_size\cf7 \}\\n\cf5 "\
            \cf2 for \cf3 nutrient \cf2 in \cf3 nutrients:\
                \cf2 if \cf3 nutrient[\cf5 'nutrientName'\cf3 ] == \cf5 'Energy'\cf3 :\
                    calories = nutrient[\cf5 'value'\cf3 ]\
                    unit = nutrient[\cf5 'unitName'\cf3 ]\
                    payload[\cf5 'content'\cf3 ] += \cf5 f"**Calories:** \cf7 \{\cf3 calories\cf7 \} \{\cf3 unit\cf7 \}\cf5  per serving\cf7 \\n\cf5 "\
            
\f1\i \cf4 # send the payload to the Discord webhook\
            
\f0\i0 \cf3 headers = \{\
                \cf5 'Content-Type'\cf3 : \cf5 'application/json'\
            \cf3 \}\
            requests.post(webhook_url, headers=headers, data=json.dumps(payload))\
        \cf2 else\cf3 :\
            payload[\cf5 'content'\cf3 ] = \cf5 f"No results found for \cf7 \{\cf3 food\cf7 \}\\n\cf5 "\
            
\f1\i \cf4 # send the payload to the Discord webhook\
            
\f0\i0 \cf3 headers = \{\
                \cf5 'Content-Type'\cf3 : \cf5 'application/json'\
            \cf3 \}\
            requests.post(webhook_url, headers=headers, data=json.dumps(payload))\
\
    write(message=\cf5 "\cf7 \\n\cf5 NOW RETRIEVING THE NUTRITION FACTS\cf7 \\n\\n\\n\cf5 "\cf3 )\
\
\
\cf2 def \cf3 display_facts():\
    
\f1\i \cf4 # set the API endpoint and API key\
    
\f0\i0 \cf3 endpoint = \cf5 "https://api.nal.usda.gov/fdc/v1/search"\
    \cf3 api_key = \cf5 "QpsCiLx41euREJtAnTqeSLyG4X6gMq5SCVN0tPJX"\
    
\f1\i \cf4 # read the list of food items from a text file\
    
\f0\i0 \cf2 with \cf3 open(\cf5 "/home/fruit/CAPSTONE/PREDICTED/predictions.txt"\cf3 , \cf5 "r"\cf3 ) \cf2 as \cf3 f:\
        foods = f.read().splitlines()\
    
\f1\i \cf4 # loop over each food item and search the API for nutrition facts\
    
\f0\i0 \cf3 nutrition_info = []\
    \cf2 for \cf3 food \cf2 in \cf3 foods:\
        params = \{\
            \cf5 "api_key"\cf3 : api_key,\
            \cf5 "generalSearchInput"\cf3 : food,\
            \cf5 "requireAllWords"\cf3 : \cf5 "true"\cf3 ,\
            \cf5 "pageSize"\cf3 : \cf5 "1"\cf3 ,\
            \cf5 "sortField"\cf3 : \cf5 "dataType.keyword"\cf3 ,\
            \cf5 "sortDirection"\cf3 : \cf5 "desc"\
        \cf3 \}\
        response = requests.get(endpoint, params=params).json()\
        \cf2 if \cf3 response[\cf5 "foods"\cf3 ]:\
            item = response[\cf5 "foods"\cf3 ][\cf6 0\cf3 ]\
            nutrients = item[\cf5 "foodNutrients"\cf3 ]\
            food_info = \{\
                \cf5 "food_name"\cf3 : item[\cf5 "description"\cf3 ],\
                \cf5 "serving_size"\cf3 : item.get(\cf5 "servingSize"\cf3 , \cf5 "N/A"\cf3 ),\
                \cf5 "calories"\cf3 : \cf2 None\
            \cf3 \}\
            \cf2 for \cf3 nutrient \cf2 in \cf3 nutrients:\
                \cf2 if \cf3 nutrient[\cf5 "nutrientName"\cf3 ] == \cf5 "Energy"\cf3 :\
                    food_info[\cf5 "calories"\cf3 ] = nutrient[\cf5 "value"\cf3 ]\
            nutrition_info.append(food_info)\
        \cf2 else\cf3 :\
            print(\cf5 f"No results found for \cf7 \{\cf3 food\cf7 \}\\n\cf5 "\cf3 )\
    \cf2 return \cf3 nutrition_info\
\
\
\cf2 def \cf3 display_nutrition_info(nutrition_info):\
    \cf2 for \cf3 food \cf2 in \cf3 nutrition_info:\
        print(\cf5 f"Food: \cf7 \{\cf3 food[\cf5 'food_name'\cf3 ]\cf7 \}\cf5 "\cf3 )\
        print(\cf5 f"Serving Size: \cf7 \{\cf3 food[\cf5 'serving_size'\cf3 ]\cf7 \}\cf5 "\cf3 )\
        print(\cf5 f"Calories: \cf7 \{\cf3 food[\cf5 'calories'\cf3 ]\cf7 \}\cf5  kcal"\cf3 )\
        print()\
\
\
\cf2 def \cf3 run():\
    print(\cf5 "\cf7 \\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\cf5 SCANNING THE CONTENTS OF YOUR FRIDGE\cf7 \\n\cf5 "\cf3 )\
    pic0()\
    pic1()\
    pic4()\
    scan()\
    send()\
    disco_calories()\
    
\f1\i \cf4 # sms()\
    
\f0\i0 \cf3 nutrition_info = display_facts()\
    display_nutrition_info(nutrition_info)\
    write(message=\cf5 "\cf7 \\n\cf5 TASKS COMPLETED !\cf7 \\n\cf5 "\cf3 )\
\
\
run()\
}