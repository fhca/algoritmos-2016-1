import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;


public class Inversiones {
	
	// Parejas de enteros, usados para reportar inversiones (i,j) y parejas (n,pasos) 
	public class Pareja {
		int i, j;
		public Pareja(int i, int j){
			this.i = i;
			this.j = j;
		}
		public String toString(){
			return "(" + i + ", " + j + ")";
		}
	}
	
	ArrayList<Pareja> reporta;
	int ary[];
	
	public Inversiones(int ary[]){
		this.ary = ary;
	}
	
	// Algoritmo cuadrático para encontrar las inversiones en una lista de enteros
	ArrayList<Pareja> go_cuadratico(){
		int pasos = 0;  // devolver esto para construir la gráfica
		reporta = new ArrayList<Pareja>();
		for(int i = 0; i < ary.length; i ++)
			for(int j = i + 1; j < ary.length; j ++) {
				if (ary[i] > ary[j])
					reporta.add(new Pareja(i,j));
				pasos ++;
			}
		return reporta;
	}
	
	// Algoritmo nlogn para encontrar las inversiones en una lista de enteros
	ArrayList<Pareja> go_nlogn(){
		int pasos = 0;  // devolver esto para construir la gráfica
		reporta = new ArrayList<Pareja>();
		// aquí va la modificación a merge_sort
		return reporta;
	}
	
	// imprime las Parejas n,pasos en un archivo
	static void archivar(String arch, ArrayList<Pareja> lista){
		try {
			PrintStream out = new PrintStream(new FileOutputStream(arch));
			for (int i = 0; i < lista.size(); i++){
				Pareja p = lista.get(i);
				out.println(p.i + " " + p.j);
			}
			out.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		int a [] = {2, 3, 8, 6, 1};
		Inversiones inv = new Inversiones(a);
		System.out.println(inv.go_cuadratico());
		//archivar("prueba.txt", inv.go_cuadratico());
	}
}
