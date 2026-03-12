import * as THREE from "three";
import { DRACOLoader, GLTF, GLTFLoader } from "three-stdlib";
import { setCharTimeline, setAllTimeline } from "../../utils/GsapScroll";
import { decryptFile } from "./decrypt";

const setCharacter = (
  renderer: THREE.WebGLRenderer,
  scene: THREE.Scene,
  camera: THREE.PerspectiveCamera
) => {
  const loader = new GLTFLoader();
  const dracoLoader = new DRACOLoader();
  dracoLoader.setDecoderPath("/draco/");
  loader.setDRACOLoader(dracoLoader);

  const loadCharacter = () => {
    return new Promise<GLTF | null>(async (resolve, reject) => {
      try {
        const encryptedBlob = await decryptFile(
          "/models/character.enc?v=2",
          "MyCharacter12"
        );
        const blobUrl = URL.createObjectURL(new Blob([encryptedBlob]));

        let character: THREE.Object3D;
        loader.load(
          blobUrl,
          async (gltf) => {
            character = gltf.scene;
            await renderer.compileAsync(character, camera, scene);
            character.traverse((child: any) => {
              if (child.isMesh) {
                const mesh = child as THREE.Mesh;

                // Change clothing colors to hacker/cyberpunk style (all black hoodie)
                if (mesh.material) {
                  if (mesh.name === "BODY.SHIRT" || mesh.name.toLowerCase().includes("shirt") || mesh.name.toLowerCase().includes("body")) {
                    // Black hoodie
                    const newMat = (mesh.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    newMat.color = new THREE.Color("#0a0a0a");
                    newMat.roughness = 0.8;
                    newMat.metalness = 0.1;
                    mesh.material = newMat;
                  } else if (mesh.name === "Pant" || mesh.name.toLowerCase().includes("pant") || mesh.name.toLowerCase().includes("leg")) {
                    // Black pants
                    const newMat = (mesh.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    newMat.color = new THREE.Color("#000000");
                    newMat.roughness = 0.7;
                    mesh.material = newMat;
                  } else if (mesh.name.toLowerCase().includes("shoe") || mesh.name.toLowerCase().includes("foot")) {
                    // Black shoes with slight tech shine
                    const newMat = (mesh.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    newMat.color = new THREE.Color("#1a1a1a");
                    newMat.metalness = 0.2;
                    mesh.material = newMat;
                  } else if (mesh.name.toLowerCase().includes("hand") || mesh.name.toLowerCase().includes("arm")) {
                    // Dark gloves
                    const newMat = (mesh.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    newMat.color = new THREE.Color("#2a2a2a");
                    mesh.material = newMat;
                  } else if (mesh.name.toLowerCase().includes("cap") || mesh.name.toLowerCase().includes("hat") || mesh.name.toLowerCase().includes("head") && !mesh.name.toLowerCase().includes("face")) {
                    // Remove cap - make it black like the hoodie body
                    const newMat = (mesh.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    newMat.color = new THREE.Color("#0a0a0a"); // Same as hoodie
                    newMat.roughness = 0.8;
                    newMat.metalness = 0.1;
                    mesh.material = newMat;
                  }
                }

                child.castShadow = true;
                child.receiveShadow = true;
                mesh.frustumCulled = true;
              }
            });
            // Face materials: keep original or apply dark theme
            character.traverse((c: any) => {
              if (c.isMesh) {
                const name = (c.name || "").toLowerCase();
                // Make face/head darker to match hoodie theme
                if (name.includes("face") || name.includes("cheek") || name.includes("eye")) {
                  if (c.material) {
                    const darkMat = (c.material as THREE.Material).clone() as THREE.MeshStandardMaterial;
                    darkMat.roughness = 0.7;
                    darkMat.metalness = 0.05;
                    c.material = darkMat;
                  }
                }
              }
            });
            resolve(gltf);
            setCharTimeline(character, camera);
            setAllTimeline();
            character!.getObjectByName("footR")!.position.y = 3.36;
            character!.getObjectByName("footL")!.position.y = 3.36;

            // Monitor scale is handled by GsapScroll.ts animations

            dracoLoader.dispose();
          },
          undefined,
          (error) => {
            console.error("Error loading GLTF model:", error);
            reject(error);
          }
        );
      } catch (err) {
        reject(err);
        console.error(err);
      }
    });
  };

  return { loadCharacter };
};

export default setCharacter;
