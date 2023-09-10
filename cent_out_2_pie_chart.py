import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.table import Table
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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the pie chart and legend on the left
    wedges, texts, autotexts = ax1.pie(values, labels=None, startangle=140, colors=colors, autopct='')

    # Hide the percentage labels on the pie chart
    for autotext in autotexts:
        autotext.set_visible(False)
    
    ax1.axis('equal')
    ax1.set_title(f'Distribution of OTUs in {os.path.basename(data_file).split("_")[0]}')

    # Create a legend using the legend mapping dictionary
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10) for label, color in color_mapping.items()]
    ax1.legend(handles=legend_elements, title="Taxonomic Level", loc="upper left")

    # Create a table to display taxonomic level and abundance on the right
    cell_text = [['Taxonomic Level', 'Abundance (unique reads)']] + list(data_dict.items())
    ax2.axis('off')
    table = ax2.table(cellText=cell_text, loc='center', colWidths=[0.4, 0.4])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.5, 1.5)

    # Add borders around subplots
    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(True)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
        ax.spines['right'].set_visible(True)

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
        for data_file in glob.glob(os.path.join(input_path, '*centrifugeReport.txt')):
            try:
                process_file(data_file, output_format)
            except Exception as e:
                print(f"Error processing {data_file}: {str(e)}")
    else:
        print("Invalid input path. Please provide a valid file or directory path.")

def process_file(data_file, output_format):
    with open(data_file, "r") as d_in:
        create_pie_chart(
            taxRank_dict_2_count(taxRank_OTU_dict(d_in)),
            legend_mapping,
            data_file,
            output_format
        )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_pie_charts.py input_path output_format")
        sys.exit(1)
    input_path = sys.argv[1]
    output_format = sys.argv[2]
    
    # Define the legend (label to color mapping)
    legend_mapping = {
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
