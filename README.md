# cent_2_pie
A basic java GUI (utilising python script to do the 'heavy' lifting) which takes in centrifuge reports (txt) and generates a pie chart (either pdf or png) for OTU frequency per taxonomic level. Produces a pie chart similar to the one shown below:

![alt text](https://github.com/DrATedder/cent_2_pie/blob/main/ERR1329867_fastp_trimmed_decon_centrifugeReport_chart.png "Pie chart example" | width =100)

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

