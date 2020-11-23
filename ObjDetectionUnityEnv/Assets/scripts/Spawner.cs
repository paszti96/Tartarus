using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject[] objects;
    public bool rotate_rand = false;
    public bool General_spawner = false;
    public int rotation = 0;
    private GameObject spawnThis;


    // Start is called before the first frame update
    void Start()
    {
        Spawn();
        
    }


    void Spawn(){
        spawnThis = objects[Random.Range(0, objects.Length)];
        if(rotate_rand)
            transform.rotation = Quaternion.Euler(0, Random.Range(0,360),0);
        else
        {
            transform.rotation = Quaternion.Euler(0,rotation,0);
        }
        Instantiate(spawnThis, gameObject.transform.position, transform.rotation);
    }

    // Update is called once per frame
    void Update()
    {
         if (Input.GetKeyDown(KeyCode.Space) && General_spawner)
         {
                Spawn();
         }
    }
}
