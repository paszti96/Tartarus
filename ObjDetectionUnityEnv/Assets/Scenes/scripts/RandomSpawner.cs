using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomSpawner : MonoBehaviour
{
    public GameObject[] objects;
    private GameObject spawnThis;
    public Vector3 center;
    public Vector2 size;



    public Quaternion min, max;

    // Start is called before the first frame update
    void Start()
    {
        //Spawn();
        
    }
    // void Spawn()
    // {
    //     randSpawnInt = Random.Range(0, objects.Length);
    //     //spawnPos.position = new Vector3(Random.Range(-10.0f,10.0f),0,Random.Range(-10.0f,10.0f));
    //     Vector3 spawnPos = new Vector3(Random.Range(-spawnRange.x, spawnRange.x), 1, Random.Range(-spawnRange.z, spawnRange.z));
    //     Instantiate(objects[randSpawnInt], spawnRange + transform.TransformPoint(0,0,0), gameObject.transform.rotation);
    // }

    void Spawn(){
        spawnThis = objects[Random.Range(0, objects.Length)];
        Vector3 pos = center + new Vector3(Random.Range(-size.x/2, size.x/2), 0.5f,Random.Range(-size.y/2, size.y/2));
        Instantiate(spawnThis, pos, gameObject.transform.rotation);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
            Spawn();
        
    }
}
