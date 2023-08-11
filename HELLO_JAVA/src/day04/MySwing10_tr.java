package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing10_tr extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing10_tr() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 374, 449);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫 별 수 : ");
		lblFirst.setBounds(29, 33, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝 별 수:");
		lblLast.setBounds(29, 80, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(120, 30, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setBounds(120, 77, 116, 21);
		contentPane.add(tfLast);
		tfLast.setColumns(10);
		
		JButton btn = new JButton("별그리기");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				myclick();
			}
		});
		btn.setBounds(29, 120, 207, 21);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(29, 151, 207, 249);
		contentPane.add(ta);
	}
	public String getStar(int cnt) {
		String ret ="";
		for(int i = 1; i<cnt ; i++) {
			ret += "*";
		}
		ret +="\n";
		return ret;
	}
	
	public void myclick() {
		String a = tfFirst.getText();
		String b = tfLast.getText();
		int ia = Integer.parseInt(a);
		int ib = Integer.parseInt(b);
		String str = "";
		for(int i =ia; i<=ib;i++) {
			str += getStar(i);
		}
		ta.setText(str);
	}
}
