package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;
	JLabel lblMine;
	JLabel lblCom;
	JLabel lblResult;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		
		lblMine = new JLabel("나");
		lblMine.setBounds(123, 39, 57, 15);
		contentPane.add(lblMine);
		
		lblCom = new JLabel("컴");
		lblCom.setBounds(123, 99, 57, 15);
		contentPane.add(lblCom);
		
		lblResult = new JLabel("결과");
		lblResult.setBounds(123, 161, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(192, 36, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(192, 96, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(192, 158, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				myclick();
			}
		});
		btn.setBounds(123, 214, 185, 23);
		contentPane.add(btn);
	}
	public void myclick() {
		double rnd = Math.random();
		String com = "";
		if(rnd<0.5) {
			com = "홀";
		} else {
			com = "짝";
		}
		tfCom.setText(com);
		String me = tfMine.getText();
		if(me.equals(com)) {
			tfResult.setText("승리");
		} else {
			tfResult.setText("패배");
		}
		
		
	}
}
