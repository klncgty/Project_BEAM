### Vector Search with locally and Ragie.ai

# Project BEAM

In this project, we will walk you through the steps of converting PDF files to JSON format and how to perform data retrieval using Ragie.ai. 

Additionally, you will see how to enhance efficiency with locally running retriever methods.

## 📄 Converting PDF to JSON

The first step involves converting our PDF file into JSON format. 
To accomplish this, we used the [camelot_convert_to_json.ipynb](https://github.com/klncgty/Project_BEAM/blob/main/advanced_file_extra/camelot_convert_to_json.ipynb) notebook located in the [advanced_file_ext](https://github.com/klncgty/Project_BEAM/tree/main/advanced_file_extra) folder. 
This file contains all the necessary code to transform PDF tables into JSON format.

## 🚀 Uploading JSON Data

Once we have the JSON file ready, we upload it to the Ragie.ai platform using the [raige_uploading.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/raige_uploading.py) script located in the [ragie_main](https://github.com/klncgty/Project_BEAM/tree/main/ragie_main) folder. 
This script ensures a quick and seamless upload of your JSON file to the platform.

## 🔍 Accessing Data

To access our JSON file and query the data, we use the [reach_document.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/reach_document.py) script. 
This script allows you to efficiently access the data stored in your uploaded JSON file.

## 📝 Query Execution

The technical query execution is handled by the [query.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/query.py) script. 
You can use this script to run your queries and retrieve the desired information from your JSON file.

## 📈 Evaluating Results

The above steps comprise the process of searching for data within the JSON file uploaded to Ragie.ai. 
You can perform the same tasks with less effort and fewer parameter changes by following the [Ragie.ai tutorial](https://docs.ragie.ai/docs/tutorial).

The retrieved results are those with the highest search scores as returned by the retriever. 
You can improve the accuracy of these results through trial and error.

## 🔧 Local Retriever Method

Another retriever method we utilize is the locally running method, which you can find in the [searchin_locally](https://github.com/klncgty/Project_BEAM/tree/main/searchin_locally) folder. The [vector_search.ipynb](https://github.com/klncgty/Project_BEAM/blob/main/searchin_locally/vector_search.ipynb) notebook in this folder mirrors the processes performed by the Ragie.ai application. All the procedures used in this notebook are open-source, allowing for various parameter tweaks and alternative technologies to be tested for maximum result accuracy.

