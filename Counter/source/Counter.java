import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Counter {

  JFrame theFrame;
  JPanel firstPanel;
  JPanel secondPanel;
  JPanel thirdPanel;
  JPanel panel;
  String currentPageString;
  String goalPageString;
  String untilGoalPageString;
  int currentPage;
  int goalPage;
  int untilGoalPage;
  JLabel currentPageLabel = new JLabel("current page");
  JLabel untilGoalPageLabel = new JLabel("until goal page");
  JTextField currentPageField = new JTextField();
  JTextField goalPageField = new JTextField();
  JButton submitButton = new JButton("Submit");
  JButton backButton = new JButton("-");
  JButton forwardButton = new JButton("+");
  JButton restartButton = new JButton("Restart");


  public static void main(String[] args) {
    Counter stuff = new Counter();
    stuff.go();
  }

  public void go(){
    submitButton.addActionListener(new SubmitListener());
    backButton.addActionListener(new BackListener());
    forwardButton.addActionListener(new ForwardListener());
    restartButton.addActionListener(new RestartListener());
    buildGUI();
  }

  public void buildGUI() {
    theFrame = new JFrame("Page Counter");
    theFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    panel = createFirstPanel();

    theFrame.getContentPane().add(panel);
    theFrame.pack();
    theFrame.setSize(350,200);
    theFrame.setVisible(true);
  }


  public GridLayout createDefaultLayout() {
    GridLayout layout = new GridLayout(3,2);
    layout.setHgap(0);
    layout.setVgap(20);
    return layout;
  }

  public JPanel createFirstPanel() {
    firstPanel = new JPanel();

    GridLayout layout = createDefaultLayout();

    firstPanel.setLayout(layout);
    firstPanel.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));

    firstPanel.add(new JLabel("What is your current page?"));
    firstPanel.add(currentPageField);
    firstPanel.add(new JLabel("What is your goal page?"));
    firstPanel.add(goalPageField);
    firstPanel.add(new JLabel(""));
    firstPanel.add(submitButton);

    theFrame.getRootPane().setDefaultButton(submitButton);
    return firstPanel;
  }

  public JPanel createSecondPanel() {
    secondPanel = new JPanel();
    GridLayout layout = createDefaultLayout();

    secondPanel.setLayout(layout);
    secondPanel.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));

    increaseSize(currentPageLabel);
    increaseSize(untilGoalPageLabel);

    secondPanel.add(new JLabel("Current Page:"));
    secondPanel.add(currentPageLabel);
    secondPanel.add(new JLabel("Pages Left:"));
    secondPanel.add(untilGoalPageLabel);
    secondPanel.add(backButton);
    secondPanel.add(forwardButton);
    theFrame.getRootPane().setDefaultButton(forwardButton);

    return secondPanel;
  }

  public JPanel createThirdPanel() {
    thirdPanel = new JPanel();
    BorderLayout layout = new BorderLayout();

    thirdPanel.setLayout(layout);
    thirdPanel.setBorder(BorderFactory.createEmptyBorder(10,100,10,100));

    JLabel finished = new JLabel("Finished!");
    thirdPanel.add(finished, BorderLayout.CENTER);
    finished.setHorizontalAlignment(SwingConstants.CENTER);

    thirdPanel.add(restartButton, BorderLayout.SOUTH);
    theFrame.getRootPane().setDefaultButton(restartButton);

    return thirdPanel;
  }

  public void increaseSize(JLabel label) {
    label.setFont(new Font("Arial", Font.BOLD, 20));
  }

  class SubmitListener implements ActionListener {
    public void actionPerformed(ActionEvent e) {
      try {
        currentPage = Integer.parseInt(currentPageField.getText());
        goalPage = Integer.parseInt(goalPageField.getText());
        untilGoalPage = goalPage - currentPage;

        currentPageLabel.setText(Integer.toString(currentPage));
        untilGoalPageLabel.setText(Integer.toString(untilGoalPage));

        theFrame.remove(panel);
        panel = createSecondPanel();
        theFrame.getContentPane().add(panel);
        theFrame.validate();
      } catch (NumberFormatException ex) {
        JOptionPane.showMessageDialog(new JFrame(),
                        "Sorry, you must submit integers.");
      }
    }
  }

  class BackListener implements ActionListener {
    public void actionPerformed(ActionEvent e) {
      untilGoalPage += 1;
      currentPage -= 1;
      untilGoalPageLabel.setText(Integer.toString(untilGoalPage));
      currentPageLabel.setText(Integer.toString(currentPage));
    }
  }

  class ForwardListener implements ActionListener {
    public void actionPerformed(ActionEvent e) {
      untilGoalPage -= 1;
      currentPage += 1;
      untilGoalPageLabel.setText(Integer.toString(untilGoalPage));
      currentPageLabel.setText(Integer.toString(currentPage));
      if (untilGoalPage == 0) {
        theFrame.remove(panel);
        panel = createThirdPanel();
        theFrame.getContentPane().add(panel);
        theFrame.validate();
      }
    }
  }

  class RestartListener implements ActionListener {
    public void actionPerformed(ActionEvent e) {
      currentPageField = new JTextField();
      goalPageField = new JTextField();
      theFrame.dispose();
      buildGUI();
    }
  }

}
