using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoundingBox : MonoBehaviour
{  
    public Texture aTexture;

    // Start is called before the first frame update
    void OnGUI()
    {   
        GameObject[] allObject = UnityEngine.Object.FindObjectsOfType<GameObject>();
        foreach(GameObject go in allObject)
        {
           {
                Rect bb = BoundingBox2D(go);
                GUI.DrawTexture(bb,aTexture, ScaleMode.ScaleToFit,true,10.0F, new Color(0,1,0,1), 1.0F,0);
                // DrawRect(bb, new Color(0,1,0,1));
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public static Rect BoundingBox2D (GameObject go)
    {
         
        Vector3[] vertices = go.GetComponent<MeshFilter>().mesh.vertices;

        float x1 = float.MaxValue, y1 = float.MaxValue, x2 = 0.0f, y2 = 0.0f;

        foreach (Vector3 vert in vertices)
        {
            Vector2 tmp = WorldToGUIPoint(go.transform.TransformPoint(vert));

            if (tmp.x < x1) x1 = tmp.x;
            if (tmp.x > x2) x2 = tmp.x;
            if (tmp.y < y1) y1 = tmp.y;
            if (tmp.y > y2) y2 = tmp.y;
        }

        Rect bbox = new Rect(x1, y1, x2 - x1, y2 - y1);
        Debug.Log(bbox);
        return bbox;
    }

    public static Vector2 WorldToGUIPoint(Vector3 world)
    {
        Vector2 screenPoint = Camera.main.WorldToScreenPoint(world);
        screenPoint.y = (float)Screen.height - screenPoint.y;
        return screenPoint;
    }
}
