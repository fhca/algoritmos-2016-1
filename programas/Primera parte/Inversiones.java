import java.util.ArrayList;


public class Inversiones {
	public class Inversion {
		public int i, j;
		public Inversion(int i, int j){
			this.i = i;
			this.j = j;
		}
		public String toString(){
			return "(" + i + ", " + j + ")";
		}
	}
	ArrayList<Inversion> reporta;
	int ary[];
	public Inversiones(int ary[]){
		this.ary = ary;
	}
	ArrayList<Inversion> go_cuadratico(){
		reporta = new ArrayList<Inversion>();
		for(int i = 0; i < ary.length; i ++){
			for(int j = i + 1; j < ary.length; j ++){
				if (ary[i] > ary[j]){
					reporta.add(new Inversion(i,j));
				}
			}
		}
		return reporta;
	}
	ArrayList<Inversion> go_nlogn(){
		reporta = new ArrayList<Inversion>();
		// aquí va la modificación a merge_sort
		return reporta;
	}
	
	public static void main(String[] args) {
		int a [] = {2, 3, 8, 6, 1};
		Inversiones inv = new Inversiones(a);
		System.out.println(inv.go_cuadratico());
	}
}
