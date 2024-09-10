> [!CAUTION]
> it is almost finish. Just 1 hour remaning...
![n9sjc](https://github.com/user-attachments/assets/b20b3cf3-c45a-46e6-b999-740ef49d6750)

# Project BEAM

In this project, i guide you through the process of converting PDF files to JSON format, performing data retrieval using Ragie.ai, and implementing similar operations locally. Below are the key steps and processes involved.

## 📝 PDF to JSON Conversion

The first step involves converting our PDF files into JSON format.Because json format more suitable to reach all the priceses of materials correctly because of its dict format. When we search in the descr. retriver can get its price together like below.
![image](https://github.com/user-attachments/assets/4456d506-03b8-437f-b5ae-7ddb43e4661a)

We used the [camelot_convert_to_json.ipynb](https://github.com/klncgty/Project_BEAM/blob/main/advanced_file_extra/camelot_convert_to_json.ipynb) notebook located in the [advanced_file_ext](https://github.com/klncgty/Project_BEAM/tree/main/advanced_file_extra) folder to achieve this. This notebook provides all the necessary code to extract tables from PDF files and convert them into JSON format.

In [camelot.ipynb](https://github.com/klncgty/Project_BEAM/blob/main/advanced_file_extra/camelot.ipynb), you can see and apply converting process pdf to csv. you can rearrange the whole process.

### Steps:
1. **Extract Tables:** We extracted tables from the PDF using the Camelot library.
2. **Save as JSON:** Each table was saved as a temporary JSON file.
3. **Combine JSONs:** All JSON files were combined into a single `all_tables.json` file, ensuring that paragraph descriptions were kept intact without splitting sentences.
   !! However, some paragraphs may fail to put it together. If the resource is more configured, this problem may not occur. Or  maybe, some manupilations on csv tables, got from camelot , can be useful for not facing this issue. But ı can state that this is not a big problem. !!

## 🚀 Operations in Ragie.ai

Once the PDF data is converted to JSON, we uploaded this JSON file to Ragie.ai for advanced data retrieval operations. Below are the key files and scripts used for these operations.

### JSON Uploading
- **Script:** [raige_uploading.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/raige_uploading.py)
- **Purpose:** This script uploads the JSON data to Ragie.ai, making it accessible for subsequent queries.

### Accessing Data
- **Script:** [reach_document.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/reach_document.py)
- **Purpose:** Allows you to access and retrieve data from the uploaded JSON file on Ragie.ai.
- You will have an output as below.
   ```
     {  "id": "64ca0a7b-2604-42dc-b22e-e54204ebb96d",
         "created_at": "2024-08-01T14:04:41.746519Z",
         "updated_at": "2024-08-01T14:17:07.294238Z",
         "status": "ready",
         "name": "EXAMPLE.pdf",
         "metadata": { "title": "YOUR_TITLE", "environment": "YOUR_ENV_NAME"},
         "chunk_count": 1942,
         "external_id": null}
    ```
### Query Execution
- **Script:** [query.py](https://github.com/klncgty/Project_BEAM/blob/main/ragie_main/query.py)
- **Purpose:** This script is used to execute queries against the JSON data on Ragie.ai, retrieving the most relevant results based on the search scores.
 

### Evaluating Results
- **Tutorial:** [Ragie.ai Tutorial](https://docs.ragie.ai/docs/tutorial)
- **Note:** The retrieved results are ranked based on relevance. You can enhance accuracy through trial and error by adjusting the `top_k` parameter.

## 🔧 Local Operations

In addition to the operations performed on Ragie.ai, similar processes can be executed locally using open-source tools and libraries. Below are the key scripts and methods used for local retrieval.

### Local Retriever Method
- **Folder:** [searchin_locally](https://github.com/klncgty/Project_BEAM/tree/main/searchin_locally)
- **Notebook:** [vector_search.ipynb](https://github.com/klncgty/Project_BEAM/blob/main/searchin_locally/vector_search.ipynb)
- **Purpose:** This notebook replicates the Ragie.ai operations locally. It uses open-source tools to perform vector searches, allowing for more customizable and experimental retrieval processes.

### Customization
- **Flexibility:** The local approach allows for more parameter tweaks and the use of alternative technologies to achieve the best possible results. This method is ideal for testing and optimizing retrieval strategies.

### Results based on the type of source file.
 
```
When working on PDFs, search results are not efficient in terms of price.
Because the unit price of the target material cannot be reached.
However, when working on json as a source, thanks to the dictionary structure,it is possible to bring the relevant material in the form of a dict and easily access the price information of that related material. 
```


## 🔍 More Vector Stores and Embedding Models Alternatives ((For Local))

When working with retrieval-augmented generation (RAG) or other similar tasks, choosing the right vector store and embedding model is crucial. Below is a list of popular vector stores and embedding models, along with information about their availability (open-source vs. paid).


### 📂 Vector Stores

1. **Faiss**
   - **Description:** Developed by Facebook AI, Faiss is a library for efficient similarity search and clustering of dense vectors.
   - **License:** Open Source
   - **Link:** [Faiss GitHub Repository](https://github.com/facebookresearch/faiss)

2. **Annoy**
   - **Description:** Annoy (Approximate Nearest Neighbors Oh Yeah) is a C++ library with Python bindings that supports fast approximate nearest neighbor search.
   - **License:** Open Source
   - **Link:** [Annoy GitHub Repository](https://github.com/spotify/annoy)

3. **Milvus**
   - **Description:** Milvus is an open-source vector database built to power embedding similarity search and AI applications.
   - **License:** Open Source
   - **Link:** [Milvus GitHub Repository](https://github.com/milvus-io/milvus)

4. **Weaviate**
   - **Description:** Weaviate is an open-source vector search engine that stores both objects and vectors, allowing for semantic search.
   - **License:** Open Source (Community Edition) / Paid (Enterprise Edition)
   - **Link:** [Weaviate Documentation](https://weaviate.io/developers/weaviate)

5. **Pinecone**
   - **Description:** Pinecone is a managed vector database service for high-performance similarity search.
   - **License:** Paid
   - **Link:** [Pinecone Website](https://www.pinecone.io/)

6. **Vectara**
   - **Description:** Vectara is a neural search-as-a-service platform that offers vector search capabilities.
   - **License:** Paid
   - **Link:** [Vectara Website](https://vectara.com/)

7. **Qdrant**
   - **Description:** Qdrant is a vector search engine that provides fast and scalable vector similarity search.
   - **License:** Open Source (Community Edition) / Paid (Cloud Service)
   - **Link:** [Qdrant GitHub Repository](https://github.com/qdrant/qdrant)

### 🧠 Embedding Models

1. **BERT (Bidirectional Encoder Representations from Transformers)**
   - **Description:** BERT is a transformer-based model developed by Google, designed for natural language understanding tasks.
   - **License:** Open Source
   - **Link:** [BERT GitHub Repository](https://github.com/google-research/bert)

2. **GPT-3**
   - **Description:** GPT-3 is a powerful language model developed by OpenAI, known for its capabilities in text generation and understanding.
   - **License:** Paid (via API access)
   - **Link:** [OpenAI GPT-3](https://beta.openai.com/)

3. **Sentence-BERT (SBERT)**
   - **Description:** Sentence-BERT is a modification of the BERT network that uses siamese and triplet networks to derive semantically meaningful sentence embeddings.
   - **License:** Open Source
   - **Link:** [SBERT GitHub Repository](https://github.com/UKPLab/sentence-transformers)

4. **Universal Sentence Encoder**
   - **Description:** Developed by Google, this model encodes text into high-dimensional vectors for tasks such as text classification, clustering, and semantic search.
   - **License:** Open Source
   - **Link:** [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4)

5. **CLIP (Contrastive Language-Image Pretraining)**
   - **Description:** Developed by OpenAI, CLIP is a model that can understand images and text jointly by using a multimodal approach.
   - **License:** Open Source
   - **Link:** [CLIP GitHub Repository](https://github.com/openai/CLIP)

6. **GloVe (Global Vectors for Word Representation)**
   - **Description:** GloVe is an unsupervised learning algorithm for obtaining vector representations for words.
   - **License:** Open Source
   - **Link:** [GloVe GitHub Repository](https://github.com/stanfordnlp/GloVe)

> [!TIP]
> HF and many other integration tools like llama index or langchain has open source embedding models also.

---

This README provides a comprehensive overview of the steps involved in the Project BEAM, from PDF to JSON conversion to advanced data retrieval operations, both on Ragie.ai and locally.

---


