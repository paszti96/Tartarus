using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject[] objects;
    private GameObject spawnThis;

    // Start is called before the first frame update
    void Start()
    {
        Spawn();
        
    }


    void Spawn(){
        spawnThis = objects[Random.Range(0, objects.Length)];
        transform.rotation = Quaternion.Euler(0, Random.Range(0,360),0);
        Instantiate(spawnThis, gameObject.transform.position, transform.rotation);
    }

    // Update is called once per frame
    void Update()
    {

    }
}
