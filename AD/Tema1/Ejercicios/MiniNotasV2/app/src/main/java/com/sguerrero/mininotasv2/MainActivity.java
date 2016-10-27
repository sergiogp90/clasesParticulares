package com.sguerrero.mininotasv2;

import android.content.Context;
import android.icu.util.Output;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class MainActivity extends AppCompatActivity {
    private String LAST_FILE = "last_file";

    private EditText editTextFileName, editTextFileContent;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Obtenemos los elementos EditText que vamos a utilizar.
        editTextFileName = (EditText) findViewById(R.id.edit_text_file_name);
        editTextFileContent = (EditText) findViewById(R.id.edit_text_file_content);

        /**
         * Intenta abrir el archivo 'last_file'. Si no existe, saltará una FileNotFoundException y no se hará
         * nada más, se cargaran los EditText vacíos.
         *
         * En caso de que si exista el archivo 'last_file', se abren 2 flujos de lectura:
         *  -El primero para leer el contenido de dicho archivo 'last_file', del que se obtiene el nombre
         *   de la última nota guardada, que se guarda en una variable String.
         *  -El segundo para leer la nota, al que se le pasa la variable String guardada tras leer el primer flujo
         *   y que contiene el nombre de la nota que vamos a abrir para leer.
         */
        String fileName;

        // Se declaran fuera los flujos. En este caso NO interesa utilizar un try-with-resources (el que cierra
        // los flujos automáticamente sin finally) porque el segundo flujo de lectura lo vamos a abrir
        // DESPUÉS de leer el nombre del archivo en el primer flujo.
        //
        // Es decir, que hasta que no leamos el primer archivo no sabremos cuál es la nota que tenemos
        // que abrir.
        BufferedReader br = null;
        BufferedReader br2 = null;

        try {
            // Abrimos el flujo de lectura para leer el archivo 'last_file'. Si no existe el archivo,
            // en este punto salta un FileNotFoundException (que no hace petar el programa) y no se
            // cargaran datos en los EditText
            br = new BufferedReader(new InputStreamReader(openFileInput(LAST_FILE)));

            // Leemos la primera línea, donde está el nombre del archivo.
            fileName = br.readLine();

            // Escribimos el nombre del archivo obtenido en el EditText correspondiente.
            editTextFileName.setText(fileName);

            // Abrimos el segundo flujo de lectura, al que le pasamos el nombre de la nota que queremos
            // leer.
            br2 = new BufferedReader(new InputStreamReader(openFileInput(fileName)));

            // Leemos una línea por cada iteración y la guardamos en la variable contenido, que HAY
            // que declarar ANTES del bucle while para poder usarla en la condición del WHILE.

            // Comprobamos que lo que se obtiene de leer sea DISTINTO de null, lo que significaría que
            // se ha llegado al final del archivo, con lo que hay que salir del bucle.
            String contenido;
            while ((contenido = br2.readLine()) != null) {
                // Utilizamos el método append(...) para AÑADIR al EditText la línea que leemos. Si
                // aquí utilizáramos .setText(contenido) SE PISARÍA la información en cada iteración.
                editTextFileContent.append(contenido);
                // Agregamos también un salto de línea con "\n", para que se escriban las líneas bien.
                editTextFileContent.append("\n");
            }
        } catch (FileNotFoundException e) {
            Log.e("FILE NOT FOUND", "No se ha encontrado último fichero.");
        } catch (IOException e) {
            e.printStackTrace();
        }finally{
            // Cerramos LOS DOS flujos de lectura.
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (br2 != null) {
                try {
                    br2.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    /**
     * Guardar el fichero. Se guardan 2 archivos:
     *  -El primero es el archivo con el nombre y contenido introducidos por el usuario.
     *  -El segundo un archivo llamado last_file, cuyo contenido será el nombre del último fichero
     *   para poder recuperarlo al abrir la aplicación.
     * @param view
     */
    public void doSaveFile(View view) {
        String fileName = editTextFileName.getText().toString();
        String fileContent = editTextFileContent.getText().toString();

        // Se abren los dos flujos de salida: Uno para escribir el archivo escrito por el usuario,
        // y otro para escribir el archivo last_file, que contendrá el nombre del archivo creado por el usuario.
        // para poder recuperarlo al abrir la aplicación.
        try (PrintWriter pw = new PrintWriter(new OutputStreamWriter(openFileOutput(fileName, Context.MODE_PRIVATE)));
             PrintWriter pw2 = new PrintWriter(new OutputStreamWriter(openFileOutput(LAST_FILE, Context.MODE_PRIVATE)))){

            // Escribimos el contenido del archivo del usuario.
            pw.write(fileContent);
            //Escribimos el archivo last_file con el nombre del archivo creado por el usuario.
            pw2.write(fileName);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
