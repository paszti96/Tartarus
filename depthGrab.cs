using System.IO;

using UnityEngine;
using UnityEngine.Experimental.Rendering;

namespace Unity.Simulation
{
    public class DepthGrab : MonoBehaviour
    {
        public CaptureImageEncoder.ImageFormat _imageFormat = CaptureImageEncoder.ImageFormat.Jpg;
        public float _screenCaptureInterval = 1.0f;
        public GraphicsFormat _format = GraphicsFormat.R8G8B8A8_UNorm;

        float _elapsedTime;
        string _baseDirectory;
        int _sequence = 0;
        public Camera _camera;

        void Start()
        {
            _baseDirectory = Manager.Instance.GetDirectoryFor(DataCapturePaths.ScreenCapture);
            if (_camera != null && _camera.depthTextureMode == DepthTextureMode.None)
                _camera.depthTextureMode = DepthTextureMode.Depth;
        }

        void Update()
        {
            _elapsedTime += Time.deltaTime;
            if (_elapsedTime > _screenCaptureInterval)
            {
                _elapsedTime -= _screenCaptureInterval;

                //if (Application.isBatchMode && _camera.targetTexture == null)
                //{
                RenderTexture depthTexture = new RenderTexture(_camera.pixelWidth, _camera.pixelHeight, 24, RenderTextureFormat.Depth);
                RenderTexture colorTexture = new RenderTexture(_camera.pixelWidth, _camera.pixelHeight, 0);
                //_camera.targetTexture = new RenderTexture(_camera.pixelWidth, _camera.pixelHeight, 0);
                _camera.depthTextureMode |= DepthTextureMode.Depth;
                _camera.SetTargetBuffers(colorTexture.colorBuffer, depthTexture.depthBuffer);
                //}
                //_camera.SetTargetBuffers(depthBuffer)
                RenderTexture currentRT = RenderTexture.active;
                RenderTexture.active = depthTexture;

                _camera.Render();

                Texture2D Image = new Texture2D(depthTexture.width,depthTexture.height);
                Image.ReadPixels(new Rect(0, 0, depthTexture.width, depthTexture.height), 0, 0);
                Image.Apply();
                RenderTexture.active = currentRT;

                var Bytes = Image.EncodeToPNG();
                Destroy(Image);
                File.WriteAllBytes(Path.Combine(_baseDirectory, _camera.name + _sequence + ".png"), Bytes);

                //(
                //    _camera, 
                //    _format, 
                //    Path.Combine(_baseDirectory, _camera.name + "_depth_" + _sequence + "." + _imageFormat.ToString().ToLower()),
                //    _imageFormat
                //);

                //if (!_camera.enabled)
                //    _camera.Render();

                ++_sequence;
            }
        }

        void OnValidate()
        {
            // Automatically add the camera component if there is one on this game object.
            if (_camera == null)
                _camera = GetComponent<Camera>();
        }
    }
}