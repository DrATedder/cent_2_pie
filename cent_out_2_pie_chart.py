import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob

def taxRank_OTU_dict(cent_out):
    tmp_dict = {}
    for line in cent_out:
        if not line.startswith("name"):
            OTU_name, taxRank = line.split("\t")[0], line.split("\t")[2]
            tmp_dict.setdefault(taxRank, []).append(OTU_name)
    return tmp_dict

def taxRank_dict_2_count(taxRank_dict):
    OTU_count_dict = {taxRank: len(OTU_names) for taxRank, OTU_names in taxRank_dict.items()}
    return OTU_count_dict

def create_pie_chart(data_dict, color_mapping, data_file, output_format):
    names = list(data_dict.keys())
    values = list(data_dict.values())
    colors = [color_mapping[name] for name in names]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(values, labels=names, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.axis('equal')
    ax.set_title(f'Distribution of OTUs in {os.path.basename(data_file).split("_")[0]}')

    if output_format == 'pdf':
        pdf_filename = f"{os.path.splitext(data_file)[0]}_chart.pdf"
        with PdfPages(pdf_filename) as pdf:
            pdf.savefig(fig)
        print(f"Saved pie chart to {pdf_filename}")
    elif output_format == 'png':
        png_filename = f"{os.path.splitext(data_file)[0]}_chart.png"
        plt.savefig(png_filename)
        print(f"Saved pie chart to {png_filename}")
    else:
        print("Invalid output format. Please choose 'pdf' or 'png'.")

def main(input_path, output_format):
    if os.path.isfile(input_path):
        # Single input file
        process_file(input_path, output_format)
    elif os.path.isdir(input_path):
        # Directory containing multiple input files
        for data_file in glob.glob(os.path.join(input_path, '*.txt')):
            process_file(data_file, output_format)
    else:
        print("Invalid input path. Please provide a valid file or directory path.")

def process_file(data_file, output_format):
    with open(data_file, "r") as d_in:
        create_pie_chart(
            taxRank_dict_2_count(taxRank_OTU_dict(d_in)),
            category_colors,
            data_file,
            output_format
        )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_pie_charts.py input_path output_format")
        sys.exit(1)
    input_path = sys.argv[1]
    output_format = sys.argv[2]
    
    category_colors = {
        'superkingdom': 'blue',
        'genus': 'green',
        'species': 'red',
        'order': 'grey',
        'family': 'cyan',
        'subspecies': 'pink',
        'leaf': 'brown',
        'phylum': 'purple',
        'class': 'yellow',
        'kingdom': 'orange',
    }

    main(input_path, output_format)
