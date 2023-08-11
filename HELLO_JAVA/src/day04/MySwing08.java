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

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(116, 13, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(195, 10, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				myclick();
			}
		});
		btn.setBounds(116, 38, 195, 23);
		contentPane.add(btn);
		
		
		ta = new JTextArea();
		ta.setBounds(116, 71, 195, 180);
		contentPane.add(ta);
		
	}
	
	public void myclick() {
		String a = tf.getText();
		int aa = Integer.parseInt(a);
		int res = 0;
		String result ="";
		result +=a+"단\n";
		for(int i=1;i<=9;i++) {
			// result += aa + "*" + i+"="+(aa*i)+"\n";
			res = i*aa;
			result +=res + "\n";
		
		}
		ta.setText(result);
	}
}
