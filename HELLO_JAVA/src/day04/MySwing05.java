package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.awt.event.ActionEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
//	JLabel lbl1;
//	JLabel lbl2;
//	JLabel lbl3;
//	JLabel lbl4;
//	JLabel lbl5;
//	JLabel lbl6;
	
	JLabel lbl1,lbl2,lbl3,lbl4,lbl5,lbl6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(32, 49, 27, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(77, 49, 27, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(116, 49, 27, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(161, 49, 27, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(209, 49, 27, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(259, 49, 27, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또생성하기");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				myclick();
			}
		});
		btn.setBounds(30, 91, 256, 23);
		contentPane.add(btn);
	}
// 내가 푼거	
//	public void myclick() {
//		//Random rnd = new Random();
//		//int num = (int)Math.random()*45+1;
//		
//		List<Integer> list = new ArrayList<Integer>();
//		for(int i = 1; i<=45; i++) {
//			list.add(i);
//		}
//		System.out.println(list.toString());
//		for(int i=0; i<list.size(); i++) {
//			int num = (int)(Math.random()*45);
//			int a = list.get(i);
//			int b = list.get(num);
//			list.set(i, b);
//			list.set(num, a);
//		}
//		lbl1.setText(list.get(0)+"");
//		lbl2.setText(list.get(1)+"");
//		lbl3.setText(list.get(2)+"");
//		lbl4.setText(list.get(3)+"");
//		lbl5.setText(list.get(4)+"");
//		lbl6.setText(list.get(5)+"");
//	}
// tr
	public void myclick() {
		int[] arr = new int[45]; // 배열 45개의 방으로 초기화
		for(int i=0; i<arr.length; i++) {
			arr[i] = i+1;
		}
		
		for (int i = 0; i<1000; i++) {
			int rnd =(int) (Math.random()*45);
			int a = arr[rnd];
			int b = arr[0];
			arr[0]= b;
			arr[rnd]=a;
		}
		lbl1.setText(arr[0]+"");
		lbl2.setText(arr[1]+"");
		lbl3.setText(arr[2]+"");
		lbl4.setText(arr[3]+"");
		lbl5.setText(arr[4]+"");
		lbl6.setText(arr[5]+"");
		
	}
}
