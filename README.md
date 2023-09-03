# cent_2_pie
A basic java GUI (utilising a python script to do the 'heavy' lifting) which takes in either a single centrifuge report (*_centrifugeReport.txt), or the location of a directory which contains n centrifuge reports. The programme generates a pie chart (either pdf or png, slected in app) per input file, which shows OTU frequency per taxonomic level (i.e. 'kingdom', 'family', 'genera', 'species' etc...). The resultant pie chart is likelt to be similar to the one shown below:

<img src="https://github.com/DrATedder/cent_2_pie/blob/0d5f8986bd5fc03ea9f526701a23b9715d412bec/ERR1329867_fastp_trimmed_decon_centrifugeReport_chart.png" width=50% height=50%>


## Prerequisites

Before using this application, ensure that you have the following prerequisites installed on your system:

### Java

- **Java Development Kit (JDK)**: You need to have the Java Development Kit (JDK) installed. You can download it from [Oracle's website](https://www.oracle.com/java/technologies/javase-downloads.html) or use OpenJDK.

### Python

- **Python 3**: The Python script component of this application requires Python 3. You can download Python from the [official Python website](https://www.python.org/downloads/).

- **Python Modules**: Install the required Python modules using `pip`:

  ```bash
  pip install matplotlib

## Usage

Clone or download this repository to your local machine.

Ensure that you have the necessary prerequisites installed as mentioned above.

Open a terminal or command prompt and navigate to the project directory.

Run the Java application:

    java -jar cent_2_pie.jar

Use the Java application to select the input file or folder containing centrifuge data and choose the desired output format (PDF or PNG).

Click the "Generate Pie Chart" button to process the data and generate the pie chart.

### Author

Dr. Andrew Tedder

University of Bradford

### License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

