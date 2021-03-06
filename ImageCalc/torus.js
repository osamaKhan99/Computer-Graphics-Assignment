const o = {
    slices: 8,
    loops: 20,
    inner_rad: 0.5,
    outerRad: 2,
    makeVerts() {
      this.vertices = [];
      this.indices = [];
      this.normals = [];
      this.color = { numComponents: 4, data: [255, 255, 255, 255, 255, 0, 0, 255, 0, 0, 255, 255], type: Uint8Array, }
      this.texCoords = [];
  
      for (let slice = 0; slice <= this.slices; ++slice) {
        const v = slice / this.slices;
        const slice_angle = v * 2 * Math.PI;
        const cos_slices = Math.cos(slice_angle);
        const sin_slices = Math.sin(slice_angle);
        const slice_rad = this.outerRad + this.inner_rad * cos_slices;
  
        for (let loop = 0; loop <= this.loops; ++loop) {

          const u = loop / this.loops;
          const loop_angle = u * 2 * Math.PI;
          const cos_loops = Math.cos(loop_angle);
          const sin_loops = Math.sin(loop_angle);
  
          const x = slice_rad * cos_loops;
          const y = slice_rad * sin_loops;
          const z = this.inner_rad * sin_slices;
  
          this.vertices.push(x, y, z);
          this.normals.push(
             cos_loops * sin_slices, 
             sin_loops * sin_slices, 
             cos_slices);
  
          this.texCoords.push(u);
          this.texCoords.push(v);
        }
      }
      const vertsPerSlice = this.loops + 1;
      for (let i = 0; i < this.slices; ++i) {
        let v1 = i * vertsPerSlice;
        let v2 = v1 + vertsPerSlice;
  
        for (let j = 0; j < this.loops; ++j) {
  
          this.indices.push(v1);
          this.indices.push(v1 + 1);
          this.indices.push(v2);
  
          this.indices.push(v2);
          this.indices.push(v1 + 1);
          this.indices.push(v2 + 1);
  
          v1 += 1;
          v2 += 1;
        }
      }
    },
};
  o.makeVerts();
  
  // -------------- ignore below this line -------------
  
  const gl = document.querySelector('canvas').getContext('webgl');
  const m4 = twgl.m4;
  
  const vs = `
  attribute vec4 position;
  attribute vec3 normal;
  attribute vec2 texcoord;
  uniform mat4 u_matrix;
  varying vec3 v_normal;
  void main() {
    gl_Position = u_matrix * position;
    v_normal = normal; // just for testing
    //v_normal = vec3(texcoord, 0);  // comment in to see texcoords
    gl_PointSize = 4.0;
  }
  `;
  
  const fs = `
  precision highp float;
  varying vec3 v_normal;
  void main() {
    gl_FragColor = vec4(v_normal * 0.5 + 0.5, 1);
  }
  `;
  
  const programInfo = twgl.createProgramInfo(gl, [vs, fs]);
  const bufferInfo = twgl.createBufferInfoFromArrays(gl, {
    position: o.vertices,
    normal: o.normals,
    texcoord: o.texCoords,
    color : o.color,
    indices: o.indices,
  });
  twgl.setBuffersAndAttributes(gl, programInfo, bufferInfo);
  gl.useProgram(programInfo.program);
  function render(time) {
    gl.enable(gl.DEPTH_TEST);
    gl.enable(gl.CULL_FACE);
    let mat = m4.perspective(
      45 * Math.PI / 180,  // fov
      2,    // aspect
      0.1,  // near
      100,  // far
    );
    mat = m4.translate(mat, [0, 0, -7]);
    mat = m4.rotateY(mat, time * 0.001);
    mat = m4.rotateX(mat, time * 0.0005);
    twgl.setUniforms(programInfo, { u_matrix: mat });
    twgl.drawBufferInfo(gl, bufferInfo);

    requestAnimationFrame(render);
 }
  requestAnimationFrame(render)