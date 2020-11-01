using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyMouseLook : MonoBehaviour
{
    public float mouseSensitivity = 3f;
    private float pitch, yaw;

    // Start is called before the first frame update
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        yaw += Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
        pitch -= Input.GetAxis("Mouse Y") * mouseSensitivity *Time.deltaTime;

        transform.eulerAngles = new Vector3(pitch, yaw, 0.0f);    
    }
}
