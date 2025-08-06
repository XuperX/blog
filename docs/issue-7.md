# InCeption XMI1.1 file explained

Looking into the InCeption XMI 1.1 file.
This document explains what each section in the InCeption XMI file does, from top to bottom. In this annotation, we have customized annotation layers, relationships, as well as attribute for relationships. 
The important sections are __3.1, 3.2, and 4__.
# Part 1: XMI headers
This section provides basic metadata, and is not important.
```xm
<?xml version="1.1" encoding="UTF-8"?><xmi:XMI xmlns:pos="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos.ecore" xmlns:tcas="http:///uima/tcas.ecore" xmlns:xmi="http://www.omg.org/XMI" xmlns:cas="http:///uima/cas.ecore" xmlns:tweet="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos/tweet.ecore" 
```
# Part 2: 
Document metadata, including document name and annotator names.
```
<type3:DocumentMetaData xmi:id="8" sofa="1" begin="0" end="21440"
language="x-unspecified"
documentTitle="FILENAME.txt"
documentId="admin" documentUri="admin-1/ANNOTATORNAME" collectionId="admin-1/ANNOTATORNAME"
documentBaseUri="admin-1" isLastSegment="false"/>
```
# Part 3: 
Annotations: 
1. Sentence info. How the sentence has been splited. Note the sentence boundries might not be correct. 
   ```
    <type5:Sentence xmi:id="19" sofa="1" begin="0" end="210"/>
    <type5:Sentence xmi:id="24" sofa="1" begin="211" end="360"/>
   ```
   
2. Token  level information. How the sentences are split into tokens. Note, the tokenizer behaves differently from regular tokenizers.

```
 <type5:Token xmi:id="999" sofa="1" begin="0" end="5" order="0"/>
 <type5:Token xmi:id="1012" sofa="1" begin="6" end="16" order="0"/>
```
3. Customized layers.
	3.1 Customized NER tags
	```
	<custom2:MYLABELS xmi:id="57833" sofa="1" begin="20232" end="20240"/>
	<custom2:MYLABELS xmi:id="57838" sofa="1" begin="20417" end="20437"/>
	```
	3.2 Cutomized  Relations (with directions). The relations
are specified in LayerDefinition, and the actual relation is provided aas a custom layer
	```
	<type:LayerDefinition xmi:id="58164" name="webanno.custom.RELATION1" uiName="RELATION1"/>
	<custom2:RELATION1 xmi:id="57873" sofa="1" begin="20597" end="20605" Dependent="57848" Governor="57859"/>
	<custom2:RELATION2 xmi:id="57903" sofa="1" begin="20030" end="20049" Dependent="57863" Governor="57744"/>
	```
	3.3 Metadata, what types of info can we find.
   Feature definition = property you can annotate on a given layer.
   For a feature like label on an NER layer, the tagset might be Person, Organization, Location, etc.
	For custom layers, you might have your own tagsets (e.g., Algorithm types: SVM, RandomForest, etc).
```
    <type:FeatureDefinition xmi:id="58142" layer="58135" name="Governor" uiName="Source"/>
    <type:FeatureDefinition xmi:id="58098" layer="58095" name="label" uiName="Label"/>
    <type:FeatureDefinition xmi:id="58109" layer="58106" name="role"
	<type3:TagsetDescription xmi:id="58248" sofa="1" begin="0" end="0" layer="webanno.custom.Algorithm" name="statistics attr" input="false"/>
    <type3:TagsetDescription xmi:id="58261" sofa="1" begin="0" end="0" layer="custom.Span" name="statistics attr" input="false"/>
```
4. The actual text with the location of each token. 
```
<cas:Sofa xmi:id="1" sofaNum="1" sofaID="_InitialView" mimeType="text" sofaString="Human peripheral blood mononuclear cell (PBMC) isolation and storage&#10;Whole blood (containing sodium citrate as an anti-coagulant) was purchased from MedRACS Clinic Research, (Asentral IRB study no. 2014–327 A).
<cas:View sofa="1" members="8 19 24 29 34 39 44 49 54 59 64 69 74 79 84 89 94 99 104 109 114 119 124 129 134 139 144 149 154 159 164 169 174 179 184 189 194 199 204 209 214 219 224 229 234 239 244 249 254 259 264 269 274 279 284 289 294 299 304 309 314 319 324 329 334 339 344 349 354 359 364 369 374 379 384 389 394 399 404 409 414
```