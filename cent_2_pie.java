import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

public class cent_2_pie {
    private static JFrame frame;
    private static JPanel mainPanel;
    private static JTextField selectedPathField;
    private static JTextArea chartInfoTextArea;
    private static JRadioButton pdfRadioButton;
    private static JRadioButton pngRadioButton;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createAndShowGUI();
            }
        });
    }

    private static void createAndShowGUI() {
        frame = new JFrame("Centrifuge hits per taxonomic level - pie chart App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);

        mainPanel = new JPanel(new BorderLayout());

        JPanel topPanel = createTopPanel();
        JPanel middlePanel = createMiddlePanel();
        JPanel bottomPanel = createBottomPanel();

        chartInfoTextArea = new JTextArea(10, 40);
        chartInfoTextArea.setEditable(false);
        JScrollPane chartInfoScrollPane = new JScrollPane(chartInfoTextArea);

        mainPanel.add(topPanel, BorderLayout.NORTH);
        mainPanel.add(middlePanel, BorderLayout.CENTER);
        mainPanel.add(chartInfoScrollPane, BorderLayout.EAST);
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        frame.add(mainPanel);

        // Add an "Author Info" button to the bottom panel
        JButton authorInfoButton = new JButton("Author Info");
        bottomPanel.add(authorInfoButton);

        authorInfoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Display author information in a dialog
                JOptionPane.showMessageDialog(frame, "Dr Andrew Tedder\nUniversity of Bradford", "Author Information", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        frame.setVisible(true);
    }

    private static JPanel createTopPanel() {
        JPanel topPanel = new JPanel();
        JLabel fileLabel = new JLabel("Select File/Folder:");
        selectedPathField = new JTextField(20);
        JButton browseButton = new JButton("Browse");
        topPanel.add(fileLabel);
        topPanel.add(selectedPathField);
        topPanel.add(browseButton);

        browseButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                fileChooser.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
                int returnValue = fileChooser.showOpenDialog(null); // Show the file dialog

                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    selectedPathField.setText(selectedFile.getAbsolutePath());
                }
            }
        });

        return topPanel;
    }

    private static JPanel createMiddlePanel() {
        JPanel middlePanel = new JPanel();
        JLabel formatLabel = new JLabel("Output Format:");
        pdfRadioButton = new JRadioButton("PDF");
        pngRadioButton = new JRadioButton("PNG");
        ButtonGroup formatGroup = new ButtonGroup();
        formatGroup.add(pdfRadioButton);
        formatGroup.add(pngRadioButton);
        pdfRadioButton.setSelected(true);

        middlePanel.add(formatLabel);
        middlePanel.add(pdfRadioButton);
        middlePanel.add(pngRadioButton);

        return middlePanel;
    }

    private static JPanel createBottomPanel() {
        JPanel bottomPanel = new JPanel();
        JButton generateButton = new JButton("Generate Pie Chart");
        JButton processAnotherButton = new JButton("Process Another File");
        JButton exitButton = new JButton("Exit");

        bottomPanel.add(generateButton);
        bottomPanel.add(processAnotherButton);
        bottomPanel.add(exitButton);

        generateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selectedPath = selectedPathField.getText();  // Get the selected file/folder path
                String outputFormat = pdfRadioButton.isSelected() ? "pdf" : "png";

                if (selectedPath != null && !selectedPath.isEmpty()) {
                    try {
                        // Run the Python script with the selected path and output format
                        ProcessBuilder processBuilder = new ProcessBuilder("python", "cent_out_2_pie_chart.py", selectedPath, outputFormat);
                        Process process = processBuilder.start();
                        process.waitFor();  // Wait for the Python script to finish

                        // Look for the chart file in the same location as the input file
                        File input = new File(selectedPath);
                        String chartFileName = input.getName().replaceFirst("[.][^.]+$", "_chart." + outputFormat);
                        File chartFile = new File(input.getParent(), chartFileName);

                        if (chartFile.exists()) {
                            Desktop desktop = Desktop.getDesktop();
                            desktop.open(chartFile);
                            chartInfoTextArea.setText("Chart saved as: " + chartFile.getAbsolutePath());
                        } else {
                            chartInfoTextArea.setText("Chart file not found.");
                        }
                    } catch (IOException | InterruptedException ex) {
                        ex.printStackTrace();
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Please select a valid input file or folder.");
                }
            }
        });

        processAnotherButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                selectedPathField.setText("");
                chartInfoTextArea.setText("");
            }
        });

        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        return bottomPanel;
    }
}

