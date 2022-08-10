program PolynomalFitting
  implicit none
 
  ! let us test it
  integer, parameter      :: degree = 15
  integer, parameter      :: dp = selected_real_kind(15, 307)
  integer                 :: i, j
  real(dp), dimension(15) :: x = (/ (i,i=1,15) /)
  real(dp), dimension(15) :: y
  real(dp), dimension(degree+1) :: a
  CHARACTER(LEN=60)                         :: f
 
  open(11, FILE='xc_int.dat')
  DO i = 1, 15
    READ(11,*) y(i)
  ENDDO
  a = polyfit(x, y, degree)

f='(A3,'//'*'//'(E10.3,A2,I2,A3),E10.3)'
WRITE(*,*) '**************************************'
WRITE(*,FMT=f) 'y= ', (a(j), 'x^',j-1, '+ ', j=1,degree+1)
WRITE(*,*) '**************************************'
 
  write (*, '(E10.3)') a
 
 CONTAINS

  function polyfit(vx, vy, d)
    implicit none
    integer, intent(in)                   :: d
    integer, parameter                    :: dp = selected_real_kind(15, 307)
    real(dp), dimension(d+1)              :: polyfit
    real(dp), dimension(:), intent(in)    :: vx, vy

    real(dp), dimension(:,:), allocatable :: X
    real(dp), dimension(:,:), allocatable :: XT
    real(dp), dimension(:,:), allocatable :: XTX

    integer :: i, j

    integer     :: n, lda, lwork
    integer :: info
    integer, dimension(:), allocatable :: ipiv
    real(dp), dimension(:), allocatable :: work

    n = d+1
    lda = n
    lwork = n

    allocate(ipiv(n))
    allocate(work(lwork))
    allocate(XT(n, size(vx)))
    allocate(X(size(vx), n))
    allocate(XTX(n, n))

    ! prepare the matrix
    do i = 0, d
       do j = 1, size(vx)
          X(j, i+1) = vx(j)**i
       end do
    end do

    XT  = transpose(X)
    XTX = matmul(XT, X)

    ! calls to LAPACK subs DGETRF and DGETRI
    call DGETRF(n, n, XTX, lda, ipiv, info)
    if ( info /= 0 ) then
       print *, "problem"
       return
    end if
    call DGETRI(n, XTX, lda, ipiv, work, lwork, info)
    if ( info /= 0 ) then
       print *, "problem"
       return
    end if

    polyfit = matmul( matmul(XTX, XT), vy)

    deallocate(ipiv)
    deallocate(work)
    deallocate(X)
    deallocate(XT)
    deallocate(XTX)

  end function
end program
