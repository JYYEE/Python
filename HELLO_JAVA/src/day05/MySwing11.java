package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

public class MySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn;
	List<Integer> bbg;
	JTextArea ta;
	int cnt =0;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing11 frame = new MySwing11();
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
	public MySwing11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 484, 534);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("야구게임");
		lbl.setBounds(55, 68, 108, 32);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(135, 72, 215, 26);
		contentPane.add(tf);
		tf.setColumns(10);

		btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				baseball();
			}
		});
		btn.setBounds(55, 110, 295, 26);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(55, 162, 295, 294);
		contentPane.add(ta);
		
		// 맞출 숫자 생성
		int[] list = new int[9];
		for(int i=0; i<list.length; i++) {
			list[i] = i+1;
		}
		for(int j=0; j<9; j++) {
			int rnd = (int) (Math.random()*9);
			int a = list[j];
			int b = list[rnd];
			list[j]=b;
			list[rnd]=a;
		}
		
		bbg = new ArrayList<Integer>();
		bbg.add(list[0]);
		bbg.add(list[1]);
		bbg.add(list[2]);
		//System.out.println(bbg);
	}
	
	public void baseball() {
		cnt++;
		String c = tf.getText();
		String[] cc = c.split("");
		
		int ballcnt = 0;
		int strikecnt = 0;
		for (int k=0; k<cc.length; k++) {
			int num = Integer.parseInt(cc[k]);
			if(num == bbg.get(k)) {
				strikecnt++;
			} else if(bbg.contains(num)) {
				ballcnt++;
			}
		}
		
		// 입력
		String str =ta.getText();
		str +=c +"\t" + strikecnt+"S"+ballcnt+"B\n";
		tf.setText("");
		ta.setText(str);
		if(strikecnt ==3) {
			JOptionPane alert = new JOptionPane();
			String result = "" +bbg.get(0) + bbg.get(1) + bbg.get(2);
			String msg = result + "를 " + cnt +"회만에 맞췄습니다.";  
			alert.showMessageDialog(btn, msg);
		}
	}
}
