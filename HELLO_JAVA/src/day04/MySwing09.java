package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn1;
	JButton btn2;
	JButton btn3;
	JButton btn4;
	JButton btn5;
	JButton btn6;
	JButton btn7;
	JButton btn8;
	JButton btn9;
	JButton btn0;
	JButton btnCall;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 224, 251);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 10, 156, 24);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn1 = new JButton("1");
		btn1.setBounds(12, 44, 54, 23);
		contentPane.add(btn1);
		
		
		btn2 = new JButton("2");
		btn2.setBounds(63, 44, 54, 23);
		contentPane.add(btn2);
		
		
		btn3 = new JButton("3");
		btn3.setBounds(114, 44, 54, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.setBounds(12, 77, 54, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.setBounds(63, 77, 54, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.setBounds(114, 77, 54, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.setBounds(12, 110, 54, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.setBounds(63, 110, 54, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.setBounds(114, 110, 54, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.setBounds(12, 143, 54, 23);
		contentPane.add(btn0);
		
		btnCall = new JButton("CALL");
		btnCall.setBounds(63, 143, 105, 23);
		contentPane.add(btnCall);
		
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// System.out.println(e.getSource()); // 이 안에 어떤 내용이 있는지 확인하고 btn와 관련된 것이 있나 확인 -> 내부에 text, btn정보 존재
			}
		});
		
//		btn1.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum1();
//				String num1 = btn1.getText();
//				String res = tf.getText();
//				res += num1;
//				tf.setText(res);
//			}
//
//		});
//		btn2.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum2();
//				String num2 = btn2.getText();
//				String res = tf.getText();
//				res += num2;
//				tf.setText(res);
//			}
//		});
//		btn3.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum3();
//				String num3 = btn3.getText();
//				String res = tf.getText();
//				res += num3;
//				tf.setText(res);
//			}
//		});
//		btn4.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum4();
//				String num4 = btn4.getText();
//				String res = tf.getText();
//				res += num4;
//				tf.setText(res);
//			}
//		});
//		btn5.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum5();
//				String num5 = btn5.getText();
//				String res = tf.getText();
//				res += num5;
//				tf.setText(res);
//			}
//		});
//		btn6.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum6();
//				String num6 = btn6.getText();
//				String res = tf.getText();
//				res += num6;
//				tf.setText(res);
//			}
//		});
//		btn7.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum7();
//				String num7 = btn7.getText();
//				String res = tf.getText();
//				res += num7;
//				tf.setText(res);
//			}
//		});
//		btn8.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum8();
//				String num8 = btn8.getText();
//				String res = tf.getText();
//				res += num8;
//				tf.setText(res);
//			}
//		});
//		btn9.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum9();
//				String num9 = btn9.getText();
//				String res = tf.getText();
//				res += num9;
//				tf.setText(res);
//			}
//		});
//		btn0.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clicknum0();
//				String num0 = btn0.getText();
//				String res = tf.getText();
//				res += num0;
//				tf.setText(res);
//			}
//		});
//		btnCall.addActionListener(new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				//clickcall();
//				JOptionPane alert = new JOptionPane();
//				String result = tf.getText();
//				String msg = "Calling\n" + result;  
//				alert.showMessageDialog(btnCall, msg);
//			}
//		});
	}
	
	public void myclick(ActionEvent e) {
		JButton obj = (JButton) e.getSource();
		String str = obj.getText();
		String str_old = tf.getText();
		tf.setText(str + str_old);
	}
//	public void myclick(String num) {
//		String num1 = btn1.getText();
//		String num2 = btn2.getText();
//		String num3 = btn3.getText();
//		String num4 = btn4.getText();
//		String num5 = btn5.getText();
//		String num6 = btn6.getText();
//		String num7 = btn7.getText();
//		String num8 = btn8.getText();
//		String num9 = btn9.getText();
//		String num0 = btn0.getText();
//		String result = "";
//		tf.setText(result);
//		
//	}
//	public void clicknum1() {
//		String num1 = btn1.getText();
//		String res = tf.getText();
//		res += num1;
//		tf.setText(res);
//	}
//	public void clicknum2() {
//		String num2 = btn2.getText();
//		String res = tf.getText();
//		res += num2;
//		tf.setText(res);
//	}
//	public void clicknum3() {
//		String num3 = btn3.getText();
//		String res = tf.getText();
//		res += num3;
//		tf.setText(res);
//	}
//	public void clicknum4() {
//		String num1 = btn4.getText();
//		String res = tf.getText();
//		res += num1;
//		tf.setText(res);
//	}
//	public void clicknum5() {
//		String num5 = btn5.getText();
//		String res = tf.getText();
//		res += num5;
//		tf.setText(res);
//	}
//	public void clicknum6() {
//		String num6 = btn6.getText();
//		String res = tf.getText();
//		res += num6;
//		tf.setText(res);
//	}
//	public void clicknum7() {
//		String num7 = btn7.getText();
//		String res = tf.getText();
//		res += num7;
//		tf.setText(res);
//	}
//	public void clicknum8() {
//		String num8 = btn8.getText();
//		String res = tf.getText();
//		res += num8;
//		tf.setText(res);
//	}
//	public void clicknum9() {
//		String num9 = btn9.getText();
//		String res = tf.getText();
//		res += num9;
//		tf.setText(res);
//	}
//	public void clicknum0() {
//		String num0 = btn0.getText();
//		String res = tf.getText();
//		res += num0;
//		tf.setText(res);
//	}
//	public void clickcall() {
//		JOptionPane alert = new JOptionPane();
//		String result = tf.getText();
//		String msg = "Calling\n" + result;  
//		alert.showMessageDialog(btnCall, msg);
//	}
	
}
