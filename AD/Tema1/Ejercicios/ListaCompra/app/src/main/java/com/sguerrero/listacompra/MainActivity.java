package com.sguerrero.listacompra;

import android.content.SyncStatusObserver;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private Button btnAnadir, btnResetear;
    private EditText editTextConcepto, editTextCantidad;
    private ListView listViewProductos;
    private List<String> listProductos = new ArrayList<>();
    private String nomArchivo = "archivo.csv";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTextCantidad = (EditText) findViewById(R.id.edit_text_cantidad);
        editTextConcepto = (EditText) findViewById(R.id.edit_text_concepto);

        listViewProductos = (ListView) findViewById(R.id.list_view_productos);

        leerArchivoCsv();
        cargarListView();

        btnAnadir = (Button) findViewById(R.id.btn_anadir);
        btnAnadir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int cantidad = Integer.parseInt(editTextCantidad.getText().toString());
                String concepto = editTextConcepto.getText().toString();

                escribirArchivoCsv(cantidad, concepto);
                leerArchivoCsv();
                cargarListView();

                editTextConcepto.setText("");
                editTextCantidad.setText("");
            }
        });

        btnResetear = (Button) findViewById(R.id.btn_resetear);
        btnResetear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                resetearArchivo();
                cargarListView();
            }
        });

    }

    public void resetearArchivo(){
        File dir = getFilesDir();
        File file = new File(dir, nomArchivo);
        boolean deleted = file.delete();

        Log.e("borrado", String.valueOf(deleted));
        listProductos.clear();
        cargarListView();
    }

    public void cargarListView(){
        ArrayAdapter<String> adapterProductos = new ArrayAdapter<>(MainActivity.this, android.R.layout.simple_list_item_1, listProductos);

        listViewProductos.setAdapter(adapterProductos);
    }

    public void leerArchivoCsv(){
        try (BufferedReader br = new BufferedReader(new InputStreamReader(openFileInput(nomArchivo)))){
            String linea = "";

            while((linea = br.readLine()) != null){
                String nuevoProducto = linea.split(";")[0]+" "+linea.split(";")[1];

                if(!listProductos.contains(nuevoProducto))
                    listProductos.add(nuevoProducto);
            }
        } catch (FileNotFoundException e) {
            Log.e("Archivo no encontrado", "Aún no se ha creado ninguna lista.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void escribirArchivoCsv(int cantidad, String concepto){
        try (PrintWriter pw = new PrintWriter(new OutputStreamWriter(openFileOutput(nomArchivo, MODE_APPEND)))) {
            pw.write(cantidad+";"+concepto+"\n");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
