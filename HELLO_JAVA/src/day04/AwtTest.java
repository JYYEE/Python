package day04;

import java.awt.Frame;

public class AwtTest {
	// 실행하면 종료할 때까지 계속 실행됨 
	public static void main(String[] args) {
		Frame f = new Frame();
		// setSize(width(가로), height(세로))
		f.setSize(300, 400);
		f.setVisible(true);
	}
}
