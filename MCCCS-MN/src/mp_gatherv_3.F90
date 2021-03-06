    DATA_TYPE :: mydata(:,:,:) !< \warning two dimensions are supposed constant!
    DATA_TYPE :: alldata(:,:,:)
    INTEGER, INTENT(IN) :: recvcount(:), displs(:)
    INTEGER, INTENT(IN) :: comm
#ifndef ALLGATHER
    INTEGER, INTENT(IN) :: root
#endif
    INTEGER :: ierr, npe, myid

#ifdef __MPI__

    CALL MPI_comm_size( comm, npe, ierr )
    IF (ierr/=0) CALL mp_stop(__LINE__)

    CALL MPI_comm_rank( comm, myid, ierr )
    IF (ierr/=0) CALL mp_stop(__LINE__)

    IF ( SIZE( recvcount ) < npe .OR. SIZE( displs ) < npe ) CALL mp_stop(__LINE__)

#ifndef ALLGATHER
    IF ( myid == root ) THEN
#endif

       IF ( SIZE( alldata, 3 ) < displs( npe ) + recvcount( npe ) ) CALL mp_stop(__LINE__)
       IF ( SIZE( alldata, 1 ) /= SIZE( mydata, 1 ) .OR. SIZE( alldata, 2 ) /= SIZE( mydata, 2 ) ) CALL mp_stop(__LINE__)

#ifndef ALLGATHER
    END IF
#endif

    IF ( SIZE( mydata, 3 ) < recvcount( myid + 1 ) ) CALL mp_stop(__LINE__)

#ifdef ALLGATHER
    CALL MPI_ALLGATHERV( mydata, recvcount(myid+1)*SIZE(mydata,1)*SIZE(mydata,2), MP_TYPE, &
     alldata, recvcount*SIZE(mydata,1)*SIZE(mydata,2), displs*SIZE(mydata,1)*SIZE(mydata,2), MP_TYPE, comm, ierr )
#else
    CALL MPI_GATHERV( mydata, recvcount(myid+1)*SIZE(mydata,1)*SIZE(mydata,2), MP_TYPE, &
     alldata, recvcount*SIZE(mydata,1)*SIZE(mydata,2), displs*SIZE(mydata,1)*SIZE(mydata,2), MP_TYPE, root, comm, ierr )
#endif

    IF (ierr/=0) CALL mp_stop(__LINE__)

#else
    IF ( SIZE( alldata, 1 ) /= SIZE( mydata, 1 ) .OR. SIZE( alldata, 2 ) /= SIZE( mydata, 2 ) ) CALL mp_stop(__LINE__)
    IF ( SIZE( alldata, 3 ) < recvcount( 1 ) ) CALL mp_stop(__LINE__)
    IF ( SIZE( mydata, 3  ) < recvcount( 1 ) ) CALL mp_stop(__LINE__)
    alldata( :, :, 1:recvcount( 1 ) ) = mydata( :, :, 1:recvcount( 1 ) )
#endif
    RETURN
