"""Independent CP04 mathematical scope study, not recovery of the missing v2 driver.
All inputs are synthetic. A kinetic-difference surrogate is not a full non-Abelian
Slavnov--Taylor identity. The convergent integral is not a quantum beta function.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,platform
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
SEED=20261013

def kinetic(p: np.ndarray) -> np.ndarray:
    return np.dot(p,p)*np.eye(4)-np.outer(p,p)

def main(out: Path) -> None:
    out.mkdir(parents=True,exist_ok=True)
    protocol={"seed":SEED,"n_scale":5000,"n_lorentz":2000,"n_kinetic":2000,"n_scalar_per_scale":1000,"scalar_scales":[.05,.1,.25,.5,1.],"tolerance":1e-10,"interpretation":"Independent source-motivated mathematical checks; not historical v2 reproduction, full gauge completion, experiment, or quantum UV validation."}
    (out/'PROTOCOL.json').write_text(json.dumps(protocol,indent=2))
    rng=np.random.default_rng(SEED)
    q=np.exp(rng.uniform(-6,6,5000));lam=np.exp(rng.uniform(-6,6,5000));s=np.exp(rng.uniform(-6,6,5000))
    z=(q/lam)**2;zp=(s*q/(s*lam))**2;ze=float(np.max(abs(z-zp)/np.maximum(z,1e-300)))
    ztest=np.linspace(.05,2,100);neg=float(np.median(abs(np.exp(-ztest)-np.exp(-4*ztest))))
    assert ze<protocol['tolerance'] and neg>.01
    # Boost a spacelike four-vector. Signature (+---), z=-k^2/Lambda^2.
    le=[]
    for _ in range(protocol['n_lorentz']):
        v=rng.normal(size=3);beta=rng.normal(size=3);beta=beta/np.linalg.norm(beta)*rng.uniform(.01,.85)
        b2=beta@beta;g=1/math.sqrt(1-b2);t=-g*(beta@v);x=v+(g-1)*(beta@v)*beta/b2
        zz=v@v;zzp=x@x-t*t;le.append(abs(zzp-zz)/max(zz,1e-20))
    assert max(le)<1e-10
    transverse=[];signed=[]
    for _ in range(protocol['n_kinetic']):
        p=rng.normal(size=4);K=kinetic(p);transverse.append(float(np.linalg.norm(K@p)/np.linalg.norm(p)**3))
        e=np.linalg.eigvalsh(K/(p@p));signed.append(float(np.max(abs(e-np.array([0,1,1,1])))))
    assert max(transverse)<1e-10 and max(signed)<1e-10
    # Taylor jets through degree 6, computed with exact fractions.
    jets={}
    for name in ['gaussian','rescaled_gaussian','super_gaussian','pole_mutant']:
        a=[]
        for n in range(7):
            if name=='super_gaussian':val=Fraction((-1)**(n//2),math.factorial(n//2)) if n%2==0 else Fraction(0)
            elif name=='rescaled_gaussian':val=Fraction((-2)**n,math.factorial(n))
            elif name=='pole_mutant':val=sum((Fraction((-1)**(j//4),1)*Fraction((-1)**(n-j),math.factorial(n-j)) for j in range(0,n+1,4)),Fraction(0))
            else:val=Fraction((-1)**n,math.factorial(n))
            a.append(val)
        jets[name]=a
    assert jets['gaussian'][:4]==jets['pole_mutant'][:4] and jets['gaussian'][4]!=jets['pole_mutant'][4]
    assert [jets['rescaled_gaussian'][n]/2**n for n in range(7)]==jets['gaussian']
    rows=[]
    for scale in protocol['scalar_scales']:
        errs=[];controls=[]
        for i in range(protocol['n_scalar_per_scale']):
            p=rng.normal(size=4)*scale;q=rng.normal(size=4)*scale
            # clip norms by a declared bounded sampling envelope to avoid overflow
            p=p/max(1.,np.linalg.norm(p)/3);q=q/max(1.,np.linalg.norm(q)/3)
            Kp=kinetic(p);Kq=kinetic(q);A=Kp-Kq;B=math.exp(p@p)*Kp-math.exp(q@q)*Kq
            f=float(np.sum(A*B)/np.sum(A*A));err=float(np.linalg.norm(B-f*A)/max(np.linalg.norm(B),1e-300));errs.append(err)
            qc=q*np.linalg.norm(p)/np.linalg.norm(q);Ac=Kp-kinetic(qc);Bc=math.exp(p@p)*Ac
            fc=float(np.sum(Ac*Bc)/np.sum(Ac*Ac));controls.append(float(np.linalg.norm(Bc-fc*Ac)/max(np.linalg.norm(Bc),1e-300)))
            rows.append([scale,i,float(p@p),float(q@q),f,err])
        if max(errs)<1e-5:raise AssertionError('Expected off-shell mismatch was not detected')
        if max(controls)>1e-10:raise AssertionError('Equal-norm positive control failed')
    with (out/'scalar_difference_tests.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['scale','trial','p_squared','q_squared','best_scalar','relative_tensor_residual']);w.writerows(rows)
    integrals=[];m2=.01
    for r in [1.,2.,5.,10.,100.]:
        local=.5*(math.log((r*r+m2)/m2)+m2/(r*r+m2)-1.)
        numeric=quad(lambda x:x**3/(x*x+m2)**2,0,r,epsabs=1e-10)[0]
        damped=quad(lambda x:x**3*math.exp(-2*x*x)/(x*x+m2)**2,0,r,epsabs=1e-10)[0]
        assert abs(local-numeric)<1e-9
        integrals.append({'R':r,'local':local,'damped':damped})
    limiting=quad(lambda x:x**3*math.exp(-2*x*x)/(x*x+m2)**2,0,np.inf,epsabs=1e-11)[0]
    summary={'date':'2026-10-13','seed':SEED,'study':'New independently implemented scope study; archived v2 driver not recovered','scale_relative_error_max':ze,'Q_only_rescaling_median_F_change':neg,'lorentz_relative_error_max':max(le),'transversality_residual_max':max(transverse),'normalized_eigenvalue_error_max':max(signed),'exact_jets':{k:[str(x) for x in a] for k,a in jets.items()},'finite_poles':{'gaussian':0,'rescaled_gaussian':0,'super_gaussian':0,'pole_mutant':4},'scalar_difference':[],'integrals':integrals,'damped_integral_infinite':limiting,'passed_declared_checks':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':platform.python_version(),'numpy':np.__version__}
    for scale in protocol['scalar_scales']:
        e=[r[5] for r in rows if r[0]==scale];summary['scalar_difference'].append({'scale':scale,'n':len(e),'median_relative_residual':float(np.median(e)),'min_relative_residual':min(e),'max_relative_residual':max(e)})
    (out/'RESULT.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).parent/'results');args=p.parse_args();main(args.out)
