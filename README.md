<h1>Abstract:</h1>
The project tackles the challenge of generating precise natural language captions that accurately capture visual elements within videos. Traditional methods often lack contextual relevance and granularity. The proposed Discriminative Latent Semantic Graph (D-LSG) framework comprises three synergistic components to address this. Firstly, a conditional graph mechanism refines object proposals by integrating contextual insights across video frames, optimizing object detection. Secondly, a dynamic graph module amalgamates these refined proposals into compact, semantically-rich visual words. Lastly, a discriminative validation mechanism scrutinizes generated captions by reconstructing visual words and aligning them against original descriptors, ensuring semantic fidelity.

<h1>Introduction:</h1>
Video captioning, automating natural language descriptions of videos, remains challenging due to complex spatio-temporal data involved. Existing generative models like encoder-decoders often fail to adequately capture object interactions within frames and their temporal evolution, struggling to produce semantically rich, accurate captions.

<h1>Literature Survey:</h1>
Existing works explored techniques like CNNs, RNNs, graph neural networks and reinforcement learning for video captioning, summarization and description generation. However, they had limitations like weak object proposals, inefficient visual knowledge extraction, and lack of robust caption validation.

<h1>Problem Statement and Objectives:</h1>
The core problem is generating semantically rich and accurate video captions by enhancing object proposals with spatio-temporal context, dynamically extracting high-level semantic visual knowledge, and rigorously validating generated sentences for relevance.

<h1>Proposed Methodology:</h1>
The D-LSG framework utilizes a Conditional Graph Operation integrating spatio-temporal features to refine region-level object proposals. A Latent Proposal Aggregation module condenses these into compact, high-level semantic visual words. A Discriminative Language Validator then evaluates the generated captions, reconstructing visual words to ensure semantic consistency.

<h1>Implementation:</h1> 
2D/3D CNNs and R-CNNs extract spatial, temporal, and object features from video frames. Graph neural networks refine object proposals using conditional graph operations. Dynamic graphs aggregate these into visual word embeddings, fed to LSTMs for caption generation. A discriminative module validates by reconstructing visual words and aligning with original descriptors.

<h1>Results and Discussion:</h1>
Evaluated on standard MSR-VTT and MSVD datasets using metrics like BLEU, METEOR, CIDEr and ROUGE, D-LSG outperformed prior methods by effectively leveraging spatio-temporal context, extracting semantic visual knowledge and validating outputs. Example outputs demonstrate quality improvements.

<h1>Conclusion:</h1> 
Implementing D-LSG yielded significant outcomes, validating graph modeling for capturing spatio-temporal dependencies and the effectiveness of discriminative modeling for semantic enrichment. It has practical significance for video retrieval and understanding tasks, opening new research directions in video summarization.


<h1>Proposed DLSG Framework:</h1>
![Picture1](https://github.com/ddarrsh/Semantic_Summarization_of_Videos_using_DLSG_B29/assets/120782143/571fffae-1c18-4bfa-aa1e-9c85e30cdf01)

  

<h1>Output Snapshots</h1>
![Screenshot (64)](https://github.com/ddarrsh/Semantic_Summarization_of_Videos_using_DLSG_B29/assets/120782143/068db211-358d-4948-9a6c-62dc02a2ddf3)
![Screenshot 2024-05-24 120951](https://github.com/ddarrsh/Semantic_Summarization_of_Videos_using_DLSG_B29/assets/120782143/c60a9f82-65fd-4370-83d7-e75b11a7ab1d)
![Screenshot (62)](https://github.com/ddarrsh/Semantic_Summarization_of_Videos_using_DLSG_B29/assets/120782143/4289dbdc-43c2-4416-a7bd-1b1ca8a4e8c9)


<h1>Live Demo</h1> https://huggingface.co/spaces/daarsh/Semantic_Summarization_of_Videos_B29
